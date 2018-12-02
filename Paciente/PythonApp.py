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
from .forms import *

def agregar(pk):
        data = []
        #pk = str(pk)
        #model = Paciente
        queryset = Paciente.objects.filter(id=pk)
        for a in queryset:
                print(a)
        #write_nfc = pk + ',' + str(nombre) + ',' + str(apellido) + ',' + str(sexo) + ',' + str(fecha_nacimiento) + ',' + str(sala_piso) + ',' + str(receta) + ',' + str(expediente)
        #print(write_nfc)
        proc = subprocess.Popen(['/home/pi/linux_libnfc-nci/./nfcDemoApp'
                                 , 'write', '--type=Text', '-l', 'en',
                                 '-r', str(pk) + ','])
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

