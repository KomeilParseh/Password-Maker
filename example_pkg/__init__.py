#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#secend Program
"""
Created on Sun Aug  9 15:33:37 2020

@author: parseh
"""
# power by Enigma Simulator made in Jadi!

import pickle
import random

alphabet = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|`~!@#/$%^&*()-_=+}{[]"':;?/>.<,'''

#password genartor!
def password_genarator():
    Rotor1 = list(alphabet)
    random.shuffle(Rotor1)
    Rotor1 = ''.join(Rotor1)

    Rotor2 = list(alphabet)
    random.shuffle(Rotor2)
    Rotor2 = ''.join(Rotor2)

    Rotor3 = list(alphabet)
    random.shuffle(Rotor3)
    Rotor3 = ''.join(Rotor3)

    file = open('./Password.Pass', 'wb')
    pickle.dump((Rotor1, Rotor2, Rotor3), file)
    file.close()

#call password genarator func
password_genarator()

# load password source in pickle
file = open('./Password.Pass', 'rb')
Rotor1, Rotor2, Rotor3 = pickle.load(file)
file.close()
file.close()
#print ('rotor is ....',Rotor1,'  ' ,Rotor2,'  ' ,Rotor3)
#print(len(alphabet))
def Make_password(plain):
    cipher = ""
    def reflector(char):
        return alphabet[len(alphabet)-alphabet.find(char)-1]

    def enigma_one_char(char):
        char1 = Rotor1[alphabet.find(char)]
        char2 = Rotor2[alphabet.find(char1)]
        char3 = Rotor3[alphabet.find(char2)]
        reflected = reflector(char3)
        char3 = alphabet[Rotor3.find(reflected)]
        char2 = alphabet[Rotor2.find(char3)]
        char1 = alphabet[Rotor1.find(char2)]

        return char1

    def rotate_rotors():
        global Rotor1, Rotor2, Rotor3
        Rotor1 = Rotor1[1:] + Rotor1[0]
        if state % 26:
            Rotor2 = Rotor2[1:] + Rotor2[0]
        if state % (26 * 26):
            Rotor3 = Rotor3[1:] + Rotor3[0]
    state = 0

    for char in plain:
        state += 1
        cipher += enigma_one_char(char)
        rotate_rotors()
    return cipher

print('hello')
print('******')
print('your password privesy')
pasword = str(input('pleas enter your word:  '))
zfill_num = int(input("Please Enter zfille Num:  "))

zfill_pass = pasword.zfill(zfill_num)
password = Make_password(zfill_pass)
password = list(password)
random.shuffle(password)
#a = 0
for i in range(1, 100):
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    password = Make_password(password)
    #a += 1
    #print('-->>number of tests', a)
    #print('==>pasword of tests', password)

print('your pasword is:', "------>>     ", Make_password(password))
