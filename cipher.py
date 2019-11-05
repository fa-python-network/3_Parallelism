# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:59:51 2019

@author: 181413
"""

import random
from multiprocessing import Process, Queue

def generate_key(length,ch,q=0):
    """Сгенерировать ключ данной длины рандомно из списка данных символов """
    key=str()
    for i in range(length):
        key+=random.choice(ch)
    if not q:
        return key
    return q.put(key)

def encrypt(message,key,ch,q=0):
    """Зашифровать сообщение данным ключом, оперирируя заданным списком символов. 
    Символы ключа, сгенерированные generate_key, должны быть подмножеством ch!!!!"""
    encrypted=str()
    for i in range(len(message)):
        index=ch.index(message[i])
        shift=ch.index(key[i])
        encrypted+=ch[(index+shift)%len(ch)]
    if not q:
        return encrypted
    return q.put(encrypted)

if __name__=="__main__":
    q1=Queue()
    q2=Queue()
    key=str()
    encrypted=str()
    symbols=[chr(i) for i in range(32,65)]
    latinchars=[chr(i) for i in range(65,128)]
    russianchars=[chr(i) for i in range(1040,1104)]
    chars=symbols+latinchars+russianchars
    message=input("Введите сообщение ")
    key=generate_key(len(message),chars)
    encrypted=encrypt(message,key,chars)
    print("Ключ и зашифрованное сообщение (без многопроцессности):\n{}\n{}".format(key,encrypted))
    
    key=""
    encrypted=""
    for i in range(len(message)):
        p1=Process(target=generate_key,args=(1,chars,q1,))
        p1.start()
        key+=q1.get()
        p1.join()
        p2=Process(target=encrypt,args=(message[i],key[i],chars,q2,))
        p2.start()
        encrypted+=q2.get()
        p2.join()
    print("Ключ и зашифрованное сообщение (c многопроцессностью):\n{}\n{}".format(key,encrypted))
        