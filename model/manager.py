# models
import router 
import host

# utils
import utils

# __init__ variables
WIDTH = 15
HEIGHT = 15

HOSTS_QUANTITY = 10
SIGNAL_RANGE = 3

class Manager:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.host_quantity = HOSTS_QUANTITY
        self.signal_range = SIGNAL_RANGE
        pass


    def __repr__(self):
        '''
        Returns network information.
        '''
        pass


    def send_data(self, data, sender, receiver):
        '''
        Sends a package based on its sender and receiver.
        If there's no way to get to the receiver, throws an error.
        If gets a list of hosts back, plot the route.
        '''
        pass

