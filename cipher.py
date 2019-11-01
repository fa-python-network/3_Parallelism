# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:59:51 2019

@author: 181413
"""

import random

def generate_key(length):
    global chars
    key=str()
    chars=[chr(i) for i in range(32,128)]
    for i in range(length):
        key+=random.choice(chars)
    return key

def encrypt(message,key):
    global chars
    encrypted=str()
    for i in range(len(message)):
        index=chars.index(message[i])
        shift=chars.index(key[i])
        encrypted+=chars[(index+shift)%len(chars)]
    return encrypted

def decrypt(message,key):
    global chars
    decrypted=str()
    for i in range(len(message)):
        index=chars.index(message[i])
        shift=chars.index(key[i])
        decrypted+=chars[(index-shift)]
    return decrypted

message="ashfgegfr"
key=generate_key(len(message))
print(key)
encypted=encrypt(message,key)
print(decrypt(message,key))
#print(encrypt("dgdshdhe",key))
