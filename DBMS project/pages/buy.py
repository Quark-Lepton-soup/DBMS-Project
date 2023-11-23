import streamlit as st
import mysql.connector

# Connect to MySQL database
db_config = {
    'user': 'ku',
    'password': 'NewPassword@123',
    'host': 'localhost',
    'database': 'Projects2',  # Add your actual database name
}

try:
    # Establish a connection to the MySQL server
    db_connection = mysql.connector.connect(**db_config)

    if db_connection.is_connected():
        print('Connected to MySQL server')

        # Create a cursor object
        cursor = db_connection.cursor()

        # Streamlit app
        st.title("Online Auction - Item Listing")

        # Example: Display items
        st.subheader("Available Items:")
        cursor.execute("SELECT * FROM Items")
        items_data = cursor.fetchall()

        print("Number of items:", len(items_data))  # Debugging line

        for item in items_data:
            st.write(f"**Item ID:** {item[0]}")
            st.write(f"**Item Name:** {item[2]}")
            st.write(f"**Description:** {item[3]}")
            st.write(f"**Starting Price:** ${item[4]:.2f}")

            # # Check if the image URL is not None
            
            # if item[5] is not None:
            #     st.image(item[5], caption=f"Image for {item[2]}", use_column_width=True)
            # else:
            #     st.warning("Image not available")



            # Add a button to place a bid for the item
            if st.button(f"Place Bid for {item[2]}"):
                # Add your bid functionality here
                st.success("Bid placed successfully!")

            st.write("---")  # Separator between items

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if 'db_connection' in locals() and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print('MySQL connection is closed')
