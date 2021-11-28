import time
import RPi.GPIO as GPIO
import MFRC522 as rfid
#CREAMOS UN OBJETO DE CLASE MFRC522
lectorRFID = rfid.MFRC522()
#MENSAJE DE BIENVENIDA
print("BUSCANDO TARJETAS...\n")
print("PRESIONE CTRL+C PARA DETENER EL PROCESO.\n")
#BLOQUE TRY CATCH
try:
    while True:
        #ESCANEO DE TARJETAS.
        (status,TagType) = lectorRFID.MFRC522_Request(lectorRFID.PICC_REQIDL)
        #OBTENER EL UID DE LA TARJETA
        (status,uid) = lectorRFID.MFRC522_Anticoll()
        #UNA VEZ OBTENIDO, CONTINUAMOS
        if status == lectorRFID.MI_OK:
            print("UID OBTENIDO---->\n")
            #IMPRIMIR EL UID
            print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
            time.sleep(2)
        else:
            print("UID NO OBTENIDO----X\n")
            print("Reintentando....\n")
            time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()

