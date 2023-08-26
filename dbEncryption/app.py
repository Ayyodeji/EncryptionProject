from flask import Flask, render_template, request, send_file, redirect, url_for
from Crypto.Cipher import AES, DES3
from Crypto.Random import get_random_bytes
import sqlite3
import os
from cryptography.fernet import Fernet
import sqlite3
import os

app = Flask(__name__)

# Load the secret key for Flask from the key file
with open('../secret_key.key', 'rb') as key_file:
    app.secret_key = key_file.read()

# Load the encryption key for data encryption
with open('../encryption_key.key', 'rb') as key_file:
    encryption_key = key_file.read()
fernet = Fernet(encryption_key)

# Initialize the user ID counter
# Initialize the user ID counter from the database
conn = sqlite3.connect('health_database.db')
cursor = conn.cursor()
cursor.execute('SELECT MAX(user_id) FROM health_data')
last_user_id = cursor.fetchone()[0]
conn.close()

counter = int(last_user_id) + 1 if last_user_id is not None else 1


@app.route('/')
def index():
    global counter
    return render_template('index.html', next_user_id=str(counter).zfill(2))

@app.route('/add_and_redirect', methods=['POST'])
def add_and_redirect():
    global counter
    
    age = request.form['age']
    sex = request.form['sex']
    height = request.form['height']
    weight = request.form['weight']
    diagnosis = request.form['diagnosis']
    medications = request.form['medications']
    allergies = request.form['allergies']
    past_surgeries = request.form['past_surgeries']
    family_history = request.form['family_history']
    blood_group = request.form['blood_group']

    # Encrypt health data
    health_data = {
        'user_id': str(counter).zfill(2),
        'age': age,
        'sex': sex,
        'height': height,
        'weight': weight,
        'diagnosis': diagnosis,
        'medications': medications,
        'allergies': allergies,
        'past_surgeries': past_surgeries,
        'family_history': family_history,
        'blood_group': blood_group
    }
    serialized_data = str(health_data).encode()
    encrypted_data = fernet.encrypt(serialized_data)

    # Insert into the database
    conn = sqlite3.connect('health_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO health_data (user_id, age, sex, height, weight, diagnosis, medications, allergies, past_surgeries, family_history, blood_group, encrypted_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (str(counter).zfill(2), age, sex, height, weight, diagnosis, medications, allergies, past_surgeries, family_history, blood_group, encrypted_data))
    conn.commit()
    conn.close()
    
    # Increment the counter for the next user ID
    counter += 1
    
    return redirect(url_for('display_data'))

@app.route('/display_data')
def display_data():
    conn = sqlite3.connect('health_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM health_data')
    health_records = cursor.fetchall()
    conn.close()

    decrypted_health_records = []

    for record in health_records:
        decrypted_data = fernet.decrypt(record[11]).decode()
        decrypted_record = eval(decrypted_data)  # Convert the decrypted data back to a dictionary
        decrypted_record['user_id'] = record[0]  # Add user_id to the decrypted record
        decrypted_health_records.append(decrypted_record)

    return render_template('display_data.html', health_records=decrypted_health_records)

@app.route('/encrypt_and_send')
def encrypt_and_send():

    with open('health_database.db', 'rb') as db_file:
        plain_data = db_file.read()

    encrypted_data = fernet.encrypt(plain_data)

    with open('../dbDecryption/database/encrypted_health_database.db', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return send_file('../dbDecryption/database/encrypted_health_database.db', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
