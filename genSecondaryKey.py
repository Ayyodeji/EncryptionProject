import os

def generate_secondary_key():
    return os.urandom(32)  # Generate a 256-bit (32-byte) random key

def save_secondary_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_secondary_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

# Example usage
if __name__ == '__main__':
    secondary_key = generate_secondary_key()
    save_secondary_key(secondary_key, 'econdary_key.key')
    loaded_secondary_key = load_secondary_key('secondary_key.key')
    print("Generated Secondary Key:", secondary_key)
    print("Loaded Secondary Key:", loade
