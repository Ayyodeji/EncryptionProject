import sqlite3

def create_database():
    conn = sqlite3.connect('health_database.db')
    cursor = conn.cursor()

    # Create health_data table
    cursor.execute('''
        CREATE TABLE health_data (
            user_id TEXT PRIMARY KEY,
            age INTEGER NOT NULL,
            sex TEXT NOT NULL,
            height TEXT NOT NULL,
            weight TEXT NOT NULL,
            diagnosis TEXT NOT NULL,
            medications TEXT NOT NULL,
            allergies TEXT NOT NULL,
            past_surgeries TEXT NOT NULL,
            family_history TEXT NOT NULL,
            blood_group TEXT NOT NULL,
            encrypted_data BLOB NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database created successfully.")
