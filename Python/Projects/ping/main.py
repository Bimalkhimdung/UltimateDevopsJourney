
# pip install icmplib
from icmplib import ping, multiping


hosts =  multiping(['192.168.1.53','192.168.1.31'], privileged=False)

for host in hosts:
    if host.is_alive:
        print(f'{host.address} is up !')
    else:
        print(f'{host.address} is down !!')