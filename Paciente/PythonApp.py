import signal
import os
import subprocess
import sys
import sqlite3
from time import sleep
#if os.environ.get('DISPLAY') is not None:
#        from pyautogui import press
#from pynput.keyboard import Key, Controller
import psycopg2
import urllib.parse as urlparse
import os

def agregar(pk):
        data = []
        pk = str(pk)
     

        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
       
        c = con.cursor()
        c.execute("SELECT nombre, apellido, sexo, fecha_nacimiento, sala_piso, receta,"
                  "expediente from Paciente_paciente WHERE id = '%s'" % pk)
        rows = c.fetchall()
        for row in rows:
                data.append(row)
        tupleData = data[0]
        name, lastName, sexo, fecha_nac, sala_piso, receta, expediente = tupleData
        write_nfc = pk + ',' + name + ',' + lastName + ',' + sexo + ',' + fecha_nac + ',' + sala_piso + ',' + receta + ',' + expediente
        conn.close()
        #sleep(10)

        proc = subprocess.Popen(['/home/pi/linux_libnfc-nci/./nfcDemoApp'
                                 , 'write', '--type=Text', '-l', 'en',
                                 '-r', str(write_nfc) + ','])
        sleep(10)
        proc.kill()
        #if os.environ.get('DISPLAY') is not None:
        #       press('enter')
        #keyboard = Controller()
        #keyboard.press(Key.enter)
        #keyboard.release(Key.enter)

        with open("/var/www/html/Healtcare2/tag_write_status.txt", "r") as f:
            com = f.readline()

        f.close()
        erase = open("/var/www/html/Healtcare2/tag_write_status.txt", "w")
        erase.write('')
        erase.close()
        com = str(com)
        print(com)
        apr = "Write Tag OK"
        if com == apr:
            return True
        else:
            return False


def buscar():
        words = []
        id = 0

        proc = subprocess.Popen(["/home/pi/linux_libnfc-nci/./nfcDemoApp", "poll"])
        
        sleep(10)
        proc.kill()
        #if os.environ.get('DISPLAY') is not None:
        #        press('enter')
        #sleep(20)
        #keyboard = Controller()
        #keyboard.press(Key.enter)
        #keyboard.release(Key.enter)

        with open("/var/www/html/Healtcare2/tag_data.txt", "r", encoding='latin-1') as f:
            data = f.readlines()
        for line in data:
            words = line.split(",")
        f.close()
        
        print(words[0])
        id = words[0]
        erase = open("/var/www/html/Healtcare2/tag_data.txt", "w")
        erase.write('')
        erase.close()

        return id[0]

