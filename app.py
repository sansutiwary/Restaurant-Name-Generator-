import streamlit as st 
import langchain_helper 

st.title("Restaurant Name Generator")   
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian", "Italian", "Japanese", "Mexican", "French"))


if cuisine:
    
    response = langchain_helper.generateResturant(cuisine)
    st.header(response['resturant_name'])
    menu_item = response['menu_item'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_item:
        
        st.write("-", item)
    