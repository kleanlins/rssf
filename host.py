class Host:
    
    id = 0

    def __init__(self, position, signal_range):
        self.id = Host.id
        Host.id += 1
        self.position = position
        self.range = signal_range
        self.routes = list()
        self.adj_hosts = list()


    def __repr__(self):
        return f"ID:{self.id}\n" + str(self.adj_hosts)

    
    def update_adj_hosts(self):
        pass
    

    def forward_data(self, package):
        pass


