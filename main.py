
#coding=utf-8
import inspect
import socket
import os
import hashlib
from datetime import datetime
import threading
from time import time
import sys

aux = 0
NUM_HILOS = 1
def conexion():
    global aux
    global NUM_HILOS

    #Cambiar el host de acuerdo a donde se esté corriendo el servidor
    host = '127.0.0.1'
    port = 6666+aux
    port2= 5005+aux
    aux+=1
    path_archivos = "./ArchivosRecibidos"
    path_logs = "./Logs"

    BLOCK_SIZE = 65536
    conexiones = 1
    obj = socket.socket()
    obj2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # obj2.bind((host,port2))
    bytesToSend = str.encode('msgFromClient')
    obj2.sendto(bytesToSend,("127.0.0.1", 20001))

    try:
        obj.connect((host, port))
        cliente = threading.currentThread().getName()
        print("Cliente " + cliente + " conectado al servidor")
        print("Cliente " + cliente + " listo para recibir...")


        year = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        hora = datetime.now().hour
        min = datetime.now().minute
        seg = datetime.now().second

        fecha = "/" + str(year) + "-" + str(mes) + "-" + str(dia) + "-" + str(hora) + "-" + str(min) + "-" + str(
            seg) + "log"
        archivolog = path_logs + fecha + ".txt"
        file = open(archivolog, "w")

        start_time = time()
        cant_paquetes = 0
        peso_tot = 0
        while (True):
            obj.send(b"Mensaje de confirmacion. Listo para recibir un archivo")
            serverHash = obj.recv(97)
            print("Recibió el hash del archivo del servidor")
            nombre_archivo = cliente + "-Prueba-" + str(conexiones) +".txt"
            archivoPorEscribir = os.path.join(path_archivos, nombre_archivo)
            file1 = open(archivoPorEscribir, "wb")
            recibido = obj2.recvfrom(1024)
            print(recibido[0].decode())
            while len(recibido)>0:
                print("Recibiendo paquete"+str(cant_paquetes))
                file1.write(recibido[0])
                recibido = obj2.recvfrom(1024)
                cant_paquetes = cant_paquetes + 1
            print("Terminó la recepción de paquetes. Se recibió un archivo completo")
            file1.close()
            dataHash = open(archivoPorEscribir)
            file.write("\n El archivo recibido fue : " + nombre_archivo)
            file.write("\n El peso fue de :" + str(os.path.getsize(archivoPorEscribir)) + " Bytes")
            peso_tot = peso_tot + float(os.path.getsize(archivoPorEscribir))
            file.write("\n Cliente: " + cliente)

            # ------------------------------------- HASHING! ------------------------------------------------

            # print("En espera de hash por parte del servidor")
            directory_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            ruta = os.path.join(directory_path, "ArchivosRecibidos/" + nombre_archivo)
            data = open(ruta, encoding='utf-8')
            print("Verificando integridad")
            hash = hashlib.sha256()
            fb = data.read(65536)
            while len(fb) > 0:
                hash.update(fb.encode('utf-8'))
                fb = data.read(65536)
            resultadoHash = hash.hexdigest()

            if (resultadoHash == serverHash.decode('utf-8')):
                print("Integridad confirmada")
            else:
                print("Falla de integridad")
                print("Enviado por el servidor:")
                print((serverHash.decode('utf-8')))
                print("Recuperado por el cliente:")
                print((resultadoHash))

            file.write("\n Entrega exitosa: ")
            if (os.path.getsize(archivoPorEscribir) != 0):
                file.write("si")
            else:
                file.write("no")
            break
        obj.close()
        file.write("\n Cantidad de paquetes recibidos: " + str(cant_paquetes))
        file.write("\n total bytes recibidos: " + str(peso_tot))
        file.write("\n Tiempo de transferencia: " + str(time() - start_time) + "seg")
        file.close()
        print("Conexión del cliente " + cliente + " cerrada")
    except:
        print("Conexión denegada. Se llegó al máximo permitido en el servidor")


for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(target=conexion,name='Cliente'+str(num_hilo))
    hilo.start()

