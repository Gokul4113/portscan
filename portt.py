import socket
import subprocess
from _datetime import datetime

target = input("enter the target ip here to scan ? ")
def portscan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"scanniing the target {ip}")
        print("Time starting ", datetime.now())
        for port in range(10,1100):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            res = sock.connect_ex((ip, port))
            if res == 0:
                print("Port {}:open".format(port))
            sock.close()
    except socket.gaierror:
        print("Hostname couldnot be resolved ")
    except socket.error:
        print("couldnot connect to the server")
portscan(target)