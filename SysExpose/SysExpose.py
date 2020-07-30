import sys
# import psutil
# import platform
# from pathlib import *
# from datetime import datetime

action = sys.argv[1]


def Menu():
    if(action == "help"):
        Help_page()
    elif(action == "public"):
        print("Public")
    elif(action == "private"):
        print("Private")
    elif(action == "system"):
        print("System")


def Help_page():
    print('''
    ------------------------------------------------------------------
    help = Print this help dialog
    public = Find the public IP address of this system
    private = Find the private IP address of this system
    system = Display system information, such as operating system etc.
    ------------------------------------------------------------------''')


Menu()
