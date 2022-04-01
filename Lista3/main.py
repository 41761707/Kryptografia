import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from numpy import zeros

def main():
    myName = "radek"
    key = myName + (32 - len(myName))*'\0'
    message = b'\0'*128
    nonce=b'\0'*8
    with open("key.txt", "wb") as file:
        file.write(str.encode(key))

    cipher = ChaCha20.new(key=str.encode(key),nonce=nonce)
    ciphertext = cipher.encrypt(message)
    with open("encode.txt", "wb") as file:
        file.write(ciphertext)


    with open('encode.txt', 'rb') as file:
        data = file.read()
    cipher2 = ChaCha20.new(key=str.encode(key), nonce=cipher.nonce)
    plaintext = cipher2.decrypt(data)
    with open("decode.txt", "wb") as file:
        file.write(plaintext)
    print(cipher2.nonce)


if __name__ == '__main__':
    main()