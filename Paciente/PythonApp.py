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
from django.db import models
import os

def agregar(pk):
        data = []
        pk = str(pk)
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=100)
        sexo = models.CharField(max_length=6, choices=sexo_tipo)
        fecha_nacimiento = models.DateField()
        sala_piso = models.CharField(max_length=100)
        receta = models.CharField(max_length=100)
        expediente = models.CharField(max_length=100)
        DATABASE_URL = os.environ['DATABASE_URL']
        write_nfc = pk + ',' + nombre + ',' + apellido + ',' + sexo + ',' + fecha_nacimiento + ',' + sala_piso + ',' + receta + ',' + expediente

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

