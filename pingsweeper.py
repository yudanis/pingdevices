import os

results = []

def ping(hostname, device_label):
    response = os.system('ping -c 1 ' + hostname)
    if response == 0:
        results.append(hostname +" "+device_label ," is UP")
    else:
        results.append(hostname +" " +device_label + " is DOWN")


ping('10.4.22.154', 'TDAS Server biak')
ping('10.4.22.1', 'router jarkombra biak')
ping('10.150.208.1', 'router jarkombra timika')
ping('10.150.208.5', 'TOC timika')

for r in results :
    print(r+ "\n")