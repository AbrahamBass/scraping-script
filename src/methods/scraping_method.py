import os
import platform


def ClearConsole():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')