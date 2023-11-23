import streamlit as st
import mysql.connector

# Connect to MySQL database
db_config = {
    'user': 'ku',
    'password': 'NewPassword@123',
    'host': 'localhost',
    'database': 'Projects2',  # Add your actual database name
}

def create_user_table():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create Users table if not exists
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Users (
                User_ID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(255) NOT NULL,
                Password VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL
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

create_user_table()

# Streamlit app
st.title("Login Section")

# User input for login
username_input = st.text_input("Username:")
password_input = st.text_input("Password:", type="password")

# Login button
if st.button("Login"):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            cursor = conn.cursor()

            # Check if the username and password match in the database
            query = "SELECT * FROM Users WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username_input, password_input))
            user_data = cursor.fetchone()

            if user_data:
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your username and password.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
