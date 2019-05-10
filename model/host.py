import math

class Host:
    '''
    A Host is defined by it's address, position, signal range and status.
    '''
    
    available_address = 0

    def __init__(self, position, signal_range):
        '''
        By default a new instance of host has it's status set to 'online'.
        '''
        self.address = Host.available_address 
        Host.available_address += 1

        self.position = position
        self.range = signal_range
        self.status = "online"

        # routing data
        self.adjacent_hosts = dict()
        self.routes = dict()
        self.forwarded_packages = list()


    def __repr__(self):
        return f"{self.address}"


    def __eq__(self, other):
        return self.address == other.address


    def update_adj_hosts(self, hosts):
        '''
        Given a list of available hosts, calculate a direct line
        representing a distance in kilometers.
        '''

        for host in hosts:
            if self.address != host.address:
                if self.is_reachable(host) < self.range and host.status == "online":
                    # print(f"{self.address} can reach {host.address} with {round(self.is_reachable(host), 2)} Km")
                    self.adjacent_hosts[host] = self.is_reachable(host)


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
            return "OK"
        else:
            return "DUPLICATE"


    def find_route(self, destination, route, distance):
        '''
        Uses recursion to find a route to a destination using adjacence list.
        Returns ROUTE, DISTANCE
        '''
        if len(self.adjacent_hosts < 2):
            return route, distance

        route.append(self.address)
        
        # IF THE DESTINATION SENT AS ARGUMENT IS AN ADJACENT HOST
        if destination in self.adjacent_hosts:
            route.append(destination.address)
            return route, distance + self.adjacent_hosts[destination]
        
        s_route = []
        s_distance = 0

        for host in self.adjacent_hosts.keys():
            if host.address not in route:
                s_route, s_distance = host.find_route(destination, route, distance + self.adjacent_hosts[host])
                    
         
