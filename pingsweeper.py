import os
import bcolor

color = bcolor.bcolors
results = []

def ping(hostname, device_label):
    response = os.system('ping -c 1 ' + hostname)
    if response == 0:
        results.append(hostname +"\t"+device_label +"\tis UP")
    else:
        results.append(hostname +"\t" +device_label + "\tis DOWN")


ping('google.com', 'Google')
ping('192.168.5.235', 'Device 1')
ping('192.168.5.236', 'Device 2')
ping('192.168.5.237', 'Device 3')
ping('192.168.5.238', 'Device 4')


print ("IP\t\tDevice Name\tStatus")
for r in results :
    if r[-1:] == 'P': 
        print(color.OKGREEN + r + color.ENDC)
    else:
        print(color.FAIL + r + color.ENDC)
        
        