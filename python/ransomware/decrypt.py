#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

f = []

for file in os.listdir():
    if file == "main.py" or file == "bruh" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        f.append(file)



with open("bruh","rb") as key:
    hash = key.read()


for file in f:
        with open(file, "rb") as files:
            content = files.read()
        content_decrypted = Fernet(hash).decrypt(content)
        with open(file, "wb") as files:
            files.write(content_decrypted)

print("your file have been deeeecrypted.")