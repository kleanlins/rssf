# models
import host
import package

# utilities
import utils

class Router:
    def __init__(self, hosts):
        self.hosts = hosts
        pass

    
    def hello(self):
        '''
        Creates a list of adjacency for each host.
        '''
        for host in self.hosts:
            host.update_adj_hosts(self.hosts)


    def change_host_status(self, host):
        '''
        Based on host ID, change it's status to online or offline.
        Mainly to test routing reconfiguration.
        '''
        if self.hosts[host].status == "online":
            self.hosts[host].status = "offline"
        else:
            self.hosts[host].status = "online"

    
    def create_routes(self, host_id, dest_id):
        '''
        Creates a route to each host for each host.
        '''
        route = []

        return self.hosts[host_id].find_route(self.hosts[dest_id], route, 0)

