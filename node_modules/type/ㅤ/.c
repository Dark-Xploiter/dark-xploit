import subprocess
import sys
import importlib
import base64
import py_compile
import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def install_and_import(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Module pycryptodome tidak ditemukan. Menginstal...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
    finally:
        globals()[module_name] = importlib.import_module(module_name)

install_and_import('Crypto')

def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def create_decrypt_file(file_name, iv, ct, key_hex):
    file_name_tanpa_extension = os.path.splitext(file_name)[0]
    decrypt_code = f"""
import subprocess
import sys
import importlib
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_and_import(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Module pycryptodome tidak ditemukan. Menginstal...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
    finally:
        globals()[module_name] = importlib.import_module(module_name)

install_and_import('Crypto')
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt(iv, ct, key):
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt.decode('utf-8')

iv = '{iv}'
ct = '{ct}'

password_file = '.pw.txt'

def save_password(password):
    with open(password_file, 'w') as f:
        f.write(password)

def get_saved_password():
    if os.path.exists(password_file):
        with open(password_file, 'r') as f:
            return f.read()
    return None

def input_password():
    saved_password = get_saved_password()
    if saved_password:
        #print("Password ditemukan, menggunakan password yang disimpan.")
        return saved_password
    else:
        password = input("\\nPassword: ")
        save_password(password)
        return password

print("=== Dibutuhkan Password ===")
password = input_password()
key = bytes.fromhex(password)
try:
    decrypted_text = decrypt(iv, ct, key)
    clear_screen()
    exec(decrypted_text)
except Exception as e:
    print("Error executing encrypted code:", e)
"""

    decrypt_file_name = file_name_tanpa_extension + "_enc.py"
    with open(decrypt_file_name, "w") as f:
        f.write(decrypt_code)
    py_compile.compile(decrypt_file_name, cfile=decrypt_file_name + "c")
    os.remove(decrypt_file_name)
    os.rename(decrypt_file_name + "c", decrypt_file_name)

def main():
    print('''\033[1;31m
 .::.: Coded By Dione x Shadow Xploit :.::.''')
    file_path = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan file \033[1;31m: \033[0;37m")
    with open(file_path, 'r') as file:
        text = file.read()
    key = get_random_bytes(16)
    time.sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPassword \033[1;31m:\033[0;37m", key.hex())
    time.sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSimpan password di tempat yang aman!!")
    iv, ciphertext = encrypt(text, key)
    #print("Encrypted:", ciphertext)
    create_decrypt_file(file_path, iv, ciphertext, key.hex())
    time.sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFile encrypt telah dibuat.")
    time.sleep(0.5)
    
if __name__ == "__main__":
    main()
