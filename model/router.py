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

    def trace_route(self, data, sender, receiver):
        '''
        Creates a route based on sender, receiver and host list of adjacency.
        Return a list of hosts representing a route.
        '''
        pass

    
    def create_routes(self):
        '''
        Creates a route to each host for each host.
        '''

        for host in self.hosts:
            #host.find_route to each host thats not on its adjacence
            pass

