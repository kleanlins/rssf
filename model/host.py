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
        self.adjacent_hosts = list()
        self.routes = dict()
        self.forwarded_packages = list()


    def __repr__(self):
        return f"{self.address}"


    def __eq__(self, other):
        return self.address == other.address

    
    def __hash__(self):
        return hash((self.address,))


    def update_adj_hosts(self, hosts):
        '''
        Given a list of available hosts, calculate a direct line
        representing a distance in kilometers.
        '''

        for host in hosts:
            if self.address != host.address:
                if self.distance_to(host) < self.range and host.status == "online":
                    # print(f"{self.address} can reach {host.address} with {round(self.distance_to(host), 2)} Km")
                    self.adjacent_hosts.append(host)

        
        # self.adjacent_hosts = sorted(self.adjacent_hosts, key=lambda x: self.distance_to(x))

        # print(self.address, self.adjacent_hosts)
        for host in self.adjacent_hosts:
            print(self.address,"->", host, "d=", self.distance_to(host))


    def distance_to(self, other):
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

        print("Entered in: ", self)

        if len(self.adjacent_hosts) < 2:
            return route, distance

        route.append(self)
        
        # print("entrou no host", self, route)

        # IF THE DESTINATION SENT AS ARGUMENT IS AN ADJACENT HOST
        if destination in self.adjacent_hosts:
            print(f"{destination} é adj de {self}")
            route.append(destination)
            print(route)
            return route, distance + self.distance_to(destination)


        s_route = []
        s_distance = 0

        for host in self.adjacent_hosts:
            if host not in route:
                s_route, s_distance = host.find_route(destination, route, distance + self.distance_to(host))
                if destination in s_route:
                    print(f"achou rota {s_route} com distancia {s_distance}")
                    return s_route, s_distance
            else:
                print("theres no route for this")
                    
         
