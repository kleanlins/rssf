class Host:
    
    id = 0

    def __init__(self, position, signal_range):
        self.id = Host.id
        Host.id += 1
        self.position = position
        self.range = signal_range

        self.adjacent_hosts = list()
        self.routes = list()

        self.forwarded_packages = list()


    def __repr__(self):
        return f"ID:{self.id}\n" + str(self.adjacent_hosts)

    
    def update_adj_hosts(self, hosts):
        # calculate distance between hosts based on pythagoras
        pass
    

    def forward_data(self, package):
        self.forwarded_packages.append(package)
        pass


    def check_duplicate(self, package):
        return package in self.forwarded_packages

