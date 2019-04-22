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
        return f"ID:{self.address}\n" + str(self.adjacent_hosts)

    
    def update_adj_hosts(self, hosts):
        '''
        Given a list of available hosts, calculate a direct line
        representing a distance in kilometers.
        '''
        pass
    

    def measure_distance(self, other):
        '''
        Calculate distance between hosts based on pythagoras.
        '''
        pass


    def forward_data(self, package):
        '''
        Analyzes the package content, look for it's destination and
        forward the package if it has the address of the final host.
        '''
        self.forwarded_packages.append(package)
        pass


    def analyze_package(self, package):
        '''
        Analyze if the package has already been forwarded.
        '''
        return package in self.forwarded_packages

