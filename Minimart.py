import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_shopping = load_lottie_url("https://lottie.host/bc12fc37-dd16-4c12-8b88-6e4df4291d40/rpRephJB7T.json")

st.set_page_config(page_title="Mini Mart", layout="wide")

items = {
    "Apples": 2.0, 
    "Bread": 1.5,   
    "Milk": 1.2,     
    "Eggs": 3.0      
}

option = st.sidebar.selectbox("Select an option", ["Main Page", "Menu", "Exit"])

if option == "Main Page":
    st.title("Welcome to Mini Mart")
    st.header("Online Delivery")
    st.subheader("Grocery Store")
    st.markdown(
        "Enjoy a wide selection of fruits, vegetables, dairy, meats, and more, all handpicked for quality."
    )

elif option == "Menu":
    st.title("Available Products")

    product = st.radio("Select a product to view its price:", list(items.keys()))
    st.success(f"You selected {product}. Price: ${items[product]}")

    selected_items = st.multiselect("Select products to purchase:", list(items.keys()))

    cart = {}
    for item in selected_items:
        quantity = st.number_input(f"Enter quantity for {item}:", min_value=0.0, step=0.1, key=item + "_qty")
        cart[item] = quantity

    customer_name = st.text_input("Customer name:")

    if st.button("Bill Generated"):
        st.text("\n------ Bill Generated ------")
        st.text(f"Bill No: 000000000")
        st.text(f"Date: 01-05-2025")
        st.text(f"Customer: {customer_name}")
        total = 0
        for item, quantity in cart.items():
            if quantity > 0:
                price = items[item]
                amount = price * quantity
                total += amount
                st.text(f"{item}: {quantity} x ${price} = ${amount}")
        st.text(f"Total Amount: ${total}")
        st.title("Thank you for your purchase!")

elif option == "Exit":
    st.subheader("Thank you for shopping with us!")
    st.title("We hope to see you again soon.")

if lottie_shopping:
    st_lottie(lottie_shopping, height=300, key="shopping")
else:
    st.error("Failed to load animation.")
