# Health Data Encryption and Decryption System

The Health Data Encryption and Decryption System is a secure solution for 
protecting and managing sensitive health records. It employs encryption 
techniques to ensure the confidentiality and integrity of health data during 
storage and transmission. The system consists of two main components: the 
Sender Side (dbEncryption) and the Receiver Side (dbDecryption).

## System Requirements

- Python 3.6 or higher
- Flask (install using `pip install Flask`)
- cryptography library (install using `pip install cryptography`)

## Installation and Setup

1. Clone this repository to your local machine:


2. Navigate to the `EncryptionProject` directory:

```bash
cd EncryptionProject
```

### Sender Side (dbEncryption)

The Sender Side component is responsible for collecting, encrypting, and 
sending health records.

1. Navigate to the `dbEncryption` directory:

```bash
cd dbEncryption
```

2. Generate the encryption key and secret key files (if not provided) and 
place them in the root folder.

3. Run the Flask application:

```bash
python app.py
```

4. Access the application by opening your web browser and navigating to 
`http://127.0.0.1:5000/`.

### Receiver Side (dbDecryption)

The Receiver Side component is responsible for receiving, decrypting, and 
displaying decrypted health records.

1. Navigate to the `dbDecryption` directory:

```bash
cd dbDecryption
```

2. Generate the encryption key and secret key files (if not provided) and 
place them in the root folder.

3. Run the decryption script:

```bash
python decryptDB.py
```

4. The decrypted health records will be displayed in the terminal.

## Usage

### Sender Side (dbEncryption)

1. Access the Sender Side application by opening your web browser and 
navigating to `http://127.0.0.1:5001/`.

2. Fill in the health record details in the provided form and submit.

3. The health records will be encrypted and stored in the database.

4. You can also encrypt and send the entire database using the "Encrypt and 
Send Database" button.

### Receiver Side (dbDecryption)

1. Run the decryption script by following the steps provided in the 
"Receiver Side (dbDecryption)" section.

2. The decrypted health records will be displayed in the terminal.

## Security Considerations

- Keep the encryption key and secret key files secure and separate from the 
application code.
- Regularly update the encryption key and rotate keys as needed.
- Implement access controls to restrict access to sensitive files and data.
- Follow best practices for securing your environment and deployment.

## Conclusion

The Health Data Encryption and Decryption System provides a secure way to 
manage and protect sensitive health records. By following the installation 
and usage instructions, you can effectively use the system to encrypt, 
transmit, receive, and decrypt health data while maintaining its 
confidentiality and integrity.
