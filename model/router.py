# models
import host
import package

# utilities
import utils

class Router:
    def __init__(self, hosts):
        self.hosts = hosts

    
    def hello(self):
        '''
        Creates a list of adjacency for each host.
        '''
        for host in self.hosts:
            host.update_adj_hosts(self.hosts)

    
    def create_routes(self, host_id, dest_id):
        '''
        Creates a route to each host for each host.
        '''
        route = []

        return self.hosts[host_id].find_route(self.hosts[dest_id], route, 0)


    def forward_data(self, route, package):

        for host in route:
            host.forward_data(package)
        
        sender_host = route[0]
        receiver_host = route[-1]

        sender_host.sent_data.append(package)
        receiver_host.received_data.append(package)

