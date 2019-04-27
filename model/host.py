import math

class Host:
    
    available_address = 0

    def __init__(self, position, signal_range):
        self.address = Host.available_address 
        Host.available_address += 1

        self.position = position
        self.range = signal_range
        self.status = "online"

        # routing data
        self.adjacent_hosts = list()
        self.routes = list()
        self.forwarded_packages = list()


    def __repr__(self):
        return f"Object <Host> ID:{self.address} - {self.position} - {self.adjacent_hosts}"


    def update_adj_hosts(self, hosts):
        '''
        Given a list of available hosts, calculate a direct line
        representing a distance in kilometers.
        '''

        for host in hosts:
            if self.address != host.address:
                if self.is_reachable(host) < self.range:
                    self.adjacent_hosts.append(host)


    def is_reachable(self, other):
        '''
        Tests if a host is reachable by analyzing it's range.
        '''        

        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]

        return (dx**2 + dy **2)**0.5


    def forward_data(self, package):
        '''
        Analyzes the package content, look for it's destination and
        forward the package if it has the address of the final host.
        '''
        if package not in self.forwarded_packages:
            self.forwarded_packages.append(package)


