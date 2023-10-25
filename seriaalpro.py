import serial
import time
 
# Abrimos el puerto serie
ser=serial.Serial('/dev/ttyS1',9600)
ser.write('\n\n OPI: Puerto abierto\n\n\r')
print "\n Puerto abierto \n"
 
while 1:
    # Leemos por el puerto serie
    caracter = ser.read()
 
    # Tratamos el caracter recibido
    if caracter == 'y':
        print " Recibido el caracter y"
        ser.write(' OPI: Caracter [y] recibido\n\r')
    elif caracter == 'n':
        print " Recibido el caracter n"
        ser.write(' OPI: Caracter [n] recibido\n\r')
    else:
        print " Recibido un caracter no esperado"
        ser.write(' OPI: Caracter no esperado, envia [y] o [n]\n\r')
 
    # Esperamos 100 ms
    time.sleep(0.1)