# this program makes a port scanner.
# this script is not really useful because it takes around 48 hours to scan all the ports.

import time
import pyfiglet
import sys
import socket
from datetime import datetime

the_banner = pyfiglet.figlet_format("PORT SCANNER")
print(the_banner)

# defining a target.
target = input(print("Enter the address you want to scan:"))
time.sleep(0.5)

if len(sys.argv) == 2:

    # translating hostname to IPv4.
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

# output ander the banner.
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


try:

    # scaning ports between 1 to 65,535.
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            time.sleep(1)
            print("Port {} is open".format(port))
        s.close()

# returns an error indicator.
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
print("the program is end")
