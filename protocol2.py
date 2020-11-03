"""
Universidad del Valle de Guatemala
Cifrado de Informacion
Seccion 11
Lic. Luis Alberto Suriano
Mario Perdomo   
Augusto Alonso
Andre Rodriguez
Josue Sagastume 
Christopher Barrios
Jose Ovando

protocol2.py
Proposito: Programa que simula Scrypt
Codigo obtenido de: link: https://cryptobook.nakov.com/mac-and-key-derivation/scrypt
"""

import pyscrypt

passwd = b'p@$Sw0rD~7'
salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
N = 2048
r = 8
p = 1
derived_key_len = 32
key = pyscrypt.hash(passwd, salt, N, r, p, derived_key_len)

print("Derived key:", key.hex())

