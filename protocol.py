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

protocol.py
Proposito: Programa que simula one-time password

"""
import pyotp
import time
#pip install pyotp

# link original: https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/more-cryptographic-concepts/one-time-passwords-otp-example.html
# OTP verificado por el secreto base 32
base32secret = pyotp.random_base32()
print('Secret:', base32secret)
#el secreto se comparte entre el servidor de google y el cliente.
totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri(
    "andres.perdomo09@gmail.com",
    issuer_name="Secure App")
print(totp_uri)