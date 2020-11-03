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

protocol.py
Proposito: Programa que simula one-time password

Codigo obtenido de: https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/more-cryptographic-concepts/one-time-passwords-otp-example.html
"""
import pyotp
import time

secret = pyotp.random_base32()
print('Secret:', secret)
totp = pyotp.TOTP(secret)

token1 = totp.now()
print("Token 1: ", token1)
time.sleep(30)
token2 = totp.now()
print("Token 2: ", token2)

status = totp.verify(token1)
print("Token 1 validation: ", status)
status = totp.verify(token2)
print("Token 2 validation: ", status)


