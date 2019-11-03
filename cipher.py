# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:59:51 2019

@author: 181413
"""

import random

def generate_key(length,ch):
    """Сгенерировать ключ данной длины рандомно из списка данных символов """
    key=str()
    for i in range(length):
        key+=random.choice(ch)
    return key

def encrypt(message,key,ch):
    """Зашифровать сообщение данным ключом, оперирируя заданным списком символов. 
    Символы ключа, сгенерированные generate_key, должны быть подмножеством ch!!!!"""
    encrypted=str()
    for i in range(len(message)):
        index=ch.index(message[i])
        shift=ch.index(key[i])
        encrypted+=ch[(index+shift)%len(ch)]
    return encrypted


key=str()
ecnrypted=str()
symbols=[chr(i) for i in range(32,65)]
latinchars=[chr(i) for i in range(65,128)]
russianchars=[chr(i) for i in range(1040,1104)]
chars=symbols+latinchars+russianchars
message=input("Введите сообщение ")
key=generate_key(len(message),russianchars)
encrypted=encrypt(message,key,symbols+russianchars)
print(key+"\n"+encrypted)
