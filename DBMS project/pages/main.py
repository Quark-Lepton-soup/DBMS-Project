import streamlit as st
import pandas as pd

# Create a DataFrame to store user details temporarily
user_data = pd.DataFrame(columns=["Name", "Email", "PAN Card Number", "Address"])

def account_verification():
    st.title("Account Verification for Sellers")

    # Get user details
    name = st.text_input("Full Name:")
    email = st.text_input("Email:")
    pan_number = st.text_input("PAN Card Number:")
    address = st.text_area("Address:")

    if st.button("Submit for Verification"):
        # Validate PAN card number and address (add more validation checks if needed)
        if not pan_number or len(pan_number) != 10:
            st.error("Invalid PAN Card Number. Please enter a valid 10-digit PAN card number.")
            return
        if not address:
            st.error("Address cannot be empty. Please provide your address.")
            return

        # Add user details to the DataFrame
        user_data.loc[len(user_data)] = [name, email, pan_number, address]

        # Display a success message
        st.success("Your account is under verification. You will be notified once verified.")

def auction_page():
    st.title("Ongoing Auctions")
    
    # Add your code to display ongoing auctions here
    # You can fetch data from a database or any other source
    
    st.write("No ongoing auctions at the moment.")

def sell_item_page():
    st.title("Sell an Item")

    # Add your code for selling an item here
    # This could include a form to add details about the item, set a starting bid, etc.

    st.write("This feature is under development.")

# Display different sections based on user choice
main_option = st.radio("Choose an option:", ["View Ongoing Auctions", "Sell an Item"])

if main_option == "View Ongoing Auctions":
    auction_page()
elif main_option == "Sell an Item":
    account_verification()
    sell_item_page()
