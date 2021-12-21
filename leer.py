#!/usr/bin/env python
'''
AUTOR: JORGE ISUR BALDERAS RAMÍREZ
FECHA: 20-12-21
DESCRIPCIÓN: PROGRAMA BÁSICO PARA LEER DATOS EN 
             UNA TARJETA RFID RC-522 MEDIANTE PYTHON
'''


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()