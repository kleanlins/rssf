class Host:
    
    available_address = 0

    def __init__(self, position, signal_range):
        self.address = Host.available_address   # works as it address
        Host.available_address += 1
        self.position = position
        self.range = signal_range

        self.adjacent_hosts = list()
        self.routes = list()
        self.forwarded_packages = list()


    def __repr__(self):
        return f"ID:{self.address}\n" + str(self.adjacent_hosts)

    
    def update_adj_hosts(self, other):
        # calculate distance between hosts based on pythagoras
        pass
    

    def forward_data(self, package):
        self.forwarded_packages.append(package)
        pass


    def analyze_package(self, package):
        return package in self.forwarded_packages

