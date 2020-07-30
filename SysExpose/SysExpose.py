import sys
import psutil
import platform
from pathlib import *
from datetime import datetime

action = sys.argv[1]


def Menu():
    if(action == "help"):
        print("Help")
    elif(action == "public"):
        print("Public")
    elif(action == "private"):
        print("Private")
    elif(action == "system"):
        print("System")