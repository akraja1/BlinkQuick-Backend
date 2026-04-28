import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("BlinkQuick - Internal Control Room")

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Stock Management", "Analytics", "Orders"])

with tab1:
    st.header("Add New Items (Employee Access)")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    stock = st.number_input("Quantity", min_value=1)
    
    if st.button("Upload to Customer App"):
        data = {"id": 1, "name": name, "price": price, "stock": stock, "category": "Grocery"}
        response = requests.post("http://localhost:8000/add-product", json=data)
        st.success(response.json()['message'])

with tab2:
    st.header("Business Analytics")
    # Sample Data for Visualization
    df = pd.DataFrame({
        "Items": ["Milk", "Bread", "Eggs", "Chips"],
        "Sales": [450, 300, 120, 500]
    })
    fig = px.bar(df, x="Items", y="Sales", title="Most Selling Products")
    st.plotly_chart(fig)

with tab3:
    st.header("Live Orders")
    st.write("Current Pending Orders: 5")