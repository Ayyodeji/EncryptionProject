from flask import Flask, render_template, redirect, url_for
import sqlite3
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load the encryption key
with open('../encryption_key.key', 'rb') as key_file:
    encryption_key = key_file.read()
fernet = Fernet(encryption_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt_and_display')
def decrypt_and_display():
    # Read the encrypted database file
    with open('../dbDecryption/database/encrypted_health_database.db', 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted data as a new database file
    with open('decrypted_health_database.db', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    # Connect to the decrypted database and query data
    conn = sqlite3.connect('decrypted_health_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM health_data')
    health_records = cursor.fetchall()
    conn.close()

    return render_template('display_data.html', health_records=health_records)

if __name__ == '__main__':
    app.run(debug=True)
