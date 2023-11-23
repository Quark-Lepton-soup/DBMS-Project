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
        st.title("Auction System")

        # Example: Display users
        st.subheader("Users:")
        cursor.execute("SELECT * FROM Users")
        users_data = cursor.fetchall()
        st.table(users_data)

        # Example: Display auctions
        st.subheader("Auctions:")
        cursor.execute("SELECT * FROM Auctions")
        auctions_data = cursor.fetchall()
        st.table(auctions_data)

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if 'db_connection' in locals() and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print('MySQL connection is closed')
