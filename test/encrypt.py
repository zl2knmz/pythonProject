from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def encrypt(message, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, bytes(key.encode('utf-8')))
    padded_message = pad(message.encode('utf-8'), DES.block_size)
    return binascii.hexlify(cipher.encrypt(padded_message)).decode('utf-8').upper()


def encrypt_data(data):
    key = "r5Pn0Y9j"
    version = 1
    encrypted_data = encrypt(data, key)
    return str(len(str(version))) + str(version) + encrypted_data


def main():
    # 11A647DF43374CDCABDAE042DD38760EFC
    print('start...')
    value = "1qazXsw2.2023"
    # 9963D5D40C5CCFB62D446EA7A5F58D9A
    a = encrypt_data(value)
    print("加密数据:", a)


if __name__ == "__main__":
    main()
