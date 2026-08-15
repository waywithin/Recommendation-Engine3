from pathlib import Path
import streamlit as st
import pickle
from sklearn.metrics.pairwise import linear_kernel
from difflib import get_close_matches

BASE_DIR = Path(__file__).resolve().parent

# Load data
products = pickle.load(open(BASE_DIR / "products.pkl", "rb"))
tfidf_matrix = pickle.load(open(BASE_DIR / "tfidf_matrix.pkl", "rb"))
tfidf = pickle.load(open(BASE_DIR / "tfidf.pkl", "rb"))

st.title("Recommended Appliances")

# Search box
search = st.text_input("Search for an appliance")


# Recommendation function
def recommend(user_input):
    query_vector = tfidf.transform([user_input])

    cosine_sim = linear_kernel(tfidf_matrix, query_vector)
    max_score = cosine_sim.max()

    if max_score < 0.2:
        return None
    
    else:

        sim_score = sorted(
            list(enumerate(cosine_sim.flatten())),
            key=lambda x: x[1],
            reverse=True
        )[1:10]

        sim_index = [i[0] for i in sim_score]

        return products.iloc[sim_index]

def get_suggestions(user_input):
    product_names =  products["name"].tolist()
    matches = get_close_matches(user_input, product_names, n = 3, cutoff=0.3)
    return matches
    
# Button
if st.button("Recommend"):

    if search.strip() == "":
        st.warning("Please enter an appliance name.")
    else:
        recommendations = recommend(search)

        if recommendations is None or recommendations.empty:
        
            suggestions = get_suggestions(search)
    
            if suggestions:
                st.warning("No recommendations found.Did you mean:")

                for suggestion in suggestions:
                    st.write(suggestion)
    
            else:
                st.warning("No Recommendations Found.")
    
    
        else:
            for _, row in recommendations.iterrows():
                st.write(f"### {row['name']}")          
                st.write(row["main_category"]) 
                st.write(row["link"])         
                st.divider()
