# models
from router import Router
from host import Host

# utils
import utils
import views

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
        
        self.hosts = list()

        ## HOSTS INSTANTIATION ##
        # generates a random position and creates a host with it 
        positions = utils.generate_coordinates(HOSTS_QUANTITY, WIDTH, HEIGHT)
        for position in positions:
            self.hosts.append(Host(position, SIGNAL_RANGE))

        ## ROUTER INSTANTIATION ##
        router = Router(self.hosts)

        # gives an list of near hosts for each host
        router.discovery()


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


    def show_map(self):
        views.plot_map(self.hosts, WIDTH, HEIGHT)

    
    def reachable_hosts(self, host):
        views.plot_reachable_hosts(self.hosts)


Manager()