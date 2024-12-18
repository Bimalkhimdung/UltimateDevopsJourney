from icmplib import multiping


def ping(hosts):
    hosts_ = multiping(hosts,privileged=False)
    for host in hosts_:
        if host.is_alive:
            print(f"{host.address} is up\n")
        else:
            print(f"{host.address} is down \n")

#ping(['192.168.1.53','192.168.1.31'])

hosts__ = input("Enter the address you want to ping (comma separated or single): ")

hosts_list = [host.strip() for host in hosts__.replace(',',' ').split()]
print(hosts_list)
ping(hosts_list)
