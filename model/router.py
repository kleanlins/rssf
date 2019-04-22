# models
import host
import package

# utilities
import utils

class Router:
    def __init__(self, hosts):
        self.hosts = hosts
        pass

    
    def discovery(self):
        '''
        Creates a list of adjacency for each host.
        '''
        pass


    def change_host_status(self, host):
        '''
        Based on host ID, change it's status to online or offline.
        Mainly to test routing reconfiguration.
        '''
        pass

    def trace_route(self, data, sender, receiver):
        '''
        Creates a route based on sender, receiver and host list of adjacency.
        Return a list of hosts representing a route.
        '''
        pass