import streamlit as st 

#configure the browser tab

st.set_page_config(page_title = "Appliance Finder", layout = "wide")

home_page = st.Page("views/home.py", title = "Home", icon = "🏡")
search_page = st.Page("views/search.py", title = "Search Items", icon = "🔍")

pg = st.navigation([home_page, search_page])
pg.run()