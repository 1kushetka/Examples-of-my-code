import rsa


with open('message.txt', 'w') as f:
    f.write("The information of the letter is here!")
    
def generate_keys():
    pubkey, privkey = rsa.newkeys(512)
    
    with open('pubkey.txt', 'wb') as f:
        f.write(pubkey.save_pkcs1())  
    with open('privkey.txt', 'wb') as f:
        f.write(privkey.save_pkcs1())


def encrypt_file(file_path, pubkey_path, output_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    with open(pubkey_path, 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    
    encrypted_data = rsa.encrypt(data, pubkey)
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)


def decrypt_file(encrypted_file_path, privkey_path, output_path):
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()

    with open(privkey_path, 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())
    
    decrypted_data = rsa.decrypt(encrypted_data, privkey)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)


def sign_file(file_path, privkey_path, signature_path):
    with open(file_path, 'rb') as f:
        message = f.read()
    with open(privkey_path, 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())

    signature = rsa.sign(message, privkey, 'SHA-1')
    
    with open(signature_path, 'wb') as f:
        f.write(signature)


def verify_signature(file_path, pubkey_path, signature_path):
    with open(file_path, 'rb') as f:
        message = f.read()

    with open(pubkey_path, 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())

    with open(signature_path, 'rb') as f:
        signature = f.read()

    try:
        rsa.verify(message, signature, pubkey)
        print("Подпись подтверждена")
    except rsa.VerificationError:
        print("Подпись недействительна")


generate_keys()
encrypt_file('message.txt', 'pubkey.txt', 'encrypted_message.txt')
decrypt_file('encrypted_message.txt', 'privkey.txt', 'decrypted_message.txt')
sign_file('message.txt', 'privkey.txt', 'signature.txt')
verify_signature('message.txt', 'pubkey.txt', 'signature.txt')