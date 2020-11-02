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
Jose Ovado

protocol2.py
Proposito: Programa que simula Scrypt
"""

#pip install scrypt
#pip install pyscrypt

import pyscrypt
#link: https://cryptobook.nakov.com/mac-and-key-derivation/scrypt
salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
#explicacion:
"""
The Scrypt calculation function takes several input parameters: the password (bytes sequence),
 the salt (bytes sequence), iterations count, block size for each iteration,
 parallelism factor and the output key length (number of bytes for the derived key).
"""
passwd = b'p@$Sw0rD~7'
key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)

#When configured properly Scrypt is considered a highly secure KDF function, 
# so you can use it as general purpose password to key derivation algorithm,
# e.g. when encrypting wallets, files or app passwords.

print("Derived key:", key.hex())

