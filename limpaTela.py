import os
import platform

def limpaTela():
    so = platform.system()

    if (so.lower() == 'windows'):
        os.system('cls')
    elif (so.lower() == 'linux'):
        os.system('clear')