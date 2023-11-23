import streamlit as st
import mysql.connector

# Connect to MySQL database
db_config = {
    'user': 'ku',
    'password': 'NewPassword@123',
    'host': 'localhost',
    'database': 'Projects2',
}

def create_items_table():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create Items table if not exists
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Items (
                Item_ID INT AUTO_INCREMENT PRIMARY KEY,
                Item_Name VARCHAR(255) NOT NULL,
                Item_Description TEXT,
                Starting_Price DECIMAL(10, 2) NOT NULL,
                Image_URL VARCHAR(255),
                Seller_ID INT,
                FOREIGN KEY (Seller_ID) REFERENCES Users(User_ID)
            )
        '''
        cursor.execute(create_table_query)
        conn.commit()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

create_items_table()

# Streamlit app
st.title("Sell an Item")

# User input for item details
item_name = st.text_input("Item Name: (AS PER FOJYA AUTHENTICATION)")
item_description = st.text_area("Item Description:")
starting_price = st.number_input("Starting Price:", min_value=0.01, format="%f")
image_url = st.text_input("Image URL:")

# Seller ID (For simplicity, you can manually set the Seller ID for now)
seller_id = st.number_input("Seller ID:")

# Add item button
if st.button("Add Item"):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            cursor = conn.cursor()

            # Insert item into the Items table
            insert_query = '''
                INSERT INTO Items (Item_Name, Item_Description, Starting_Price, Image_URL, Seller_ID)
                VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (item_name, item_description, starting_price, image_url, seller_id))
            conn.commit()

            st.success("Item added successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        st.error("Error adding item. Please try again.")

    finally:
        # Close the database connection
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
