import sys
import platform
from requests import *
import socket


def Expose():
    def Help_page():
        print('''
        ------------------------------------------------------------------
        help = Print this help dialog
        public = Find the public IP address of this system
        private = Find the private IP address of this system
        system = Display system information, such as operating system etc.
        ------------------------------------------------------------------''')

    def public_ip_page():
        public_ip = get('https://api.ipify.org').text
        print("My public IP address is " + public_ip)

    def private_ip_page():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            private_ip = s.getsockname()[0]
        except Exception:
            private_ip = '127.0.0.1'
        finally:
            s.close()
        print("The private ip of this system is " + private_ip)

    def system_info_page():
        system = str(platform.system())
        arch = str(platform.architecture())
        machine = str(platform.machine())
        node = str(platform.node())
        processor = str(platform.processor())

        print("The current operating system is: " + system)
        print("The current system architecture is: " + arch)
        print("The current machine type is:  " + machine)
        print("The current hostname is: " + node)
        print("The current processor information is: " + processor)

    action = sys.argv[1]
    if (action == "help"):
        Help_page()
    elif (action == "public"):
        public_ip_page()
    elif (action == "private"):
        private_ip_page()
    elif (action == "system"):
        system_info_page()

