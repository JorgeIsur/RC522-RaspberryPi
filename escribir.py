#!/usr/bin/env python
'''
AUTOR: JORGE ISUR BALDERAS RAMÍREZ
FECHA: 20-12-21
DESCRIPCIÓN: PROGRAMA BÁSICO PARA INGRESAR DATOS EN 
             UNA TARJETA RFID RC-522 MEDIANTE PYTHON
'''


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('Nuevo dato:\n')
        print("Acerca tu tarjeta al lector\n")
        reader.write(text)
        print("Escrito\n")
finally:
        GPIO.cleanup()