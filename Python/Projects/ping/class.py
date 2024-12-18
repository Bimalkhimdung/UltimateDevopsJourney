from icmplib import ping, multiping
class ping:
    def __init__(self,hosts):
        self.hosts= [hosts] if isinstance(hosts,str) else hosts
        self.result = multiping(self.hosts, privileged=False)
    
    def __str__(self):
        result_addr = ""
        for x in self.result:
            if x.is_alive:
                result_addr += f"{x.address} is up\n"
            else:
                result_addr += f"{x.address} is down\n"
            return result_addr
ping_ = ping(["192.168.1.53","192.168.1.31"])
print(ping_)