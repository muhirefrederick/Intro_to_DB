import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (change user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mamabene@09"   # 🔑 replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database safely
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # ✅ explicit error handling
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection safely
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
