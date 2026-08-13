import streamlit as st
import pickle

st.title("High-Demand Appliances")
st.subheader("Our Most Popular Product This Week")
st.subheader("Appliances")


appliances = pickle.load(open("../popular_appliances.pkl", "rb"))

#st.dataframe(appliances.head())

top50 = appliances.head(50)
#st.write(top50.iloc[25])

for index, row in top50.iterrows():
    st.write(row["name"])
    st.write("-------")

    