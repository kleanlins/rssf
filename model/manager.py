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
SIGNAL_RANGE = 5

class Manager:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.host_quantity = HOSTS_QUANTITY
        self.signal_range = SIGNAL_RANGE
        
        self.hosts = list()

        ## HOSTS INSTANTIATION ##
        # generates a random position and creates a host with it 
        print(f"\nGenerating positions for {HOSTS_QUANTITY} hosts in a map {WIDTH}x{HEIGHT} Km...", end=" ")
        positions = utils.generate_coordinates(HOSTS_QUANTITY, WIDTH, HEIGHT)
        for position in positions:
            self.hosts.append(Host(position, SIGNAL_RANGE))
        print(f"{HOSTS_QUANTITY} hosts were created.")

        ## ROUTER INSTANTIATION ##
        print("Creating router...", end=" ")
        router = Router(self.hosts)
        print("Router created.")

        # gives an list of near active hosts for each host
        print("Running Hello for each host...", end=" ")
        router.hello()
        print("Host Hello status complete.\n")

        # now each host should discover a route to each other host
        # router.create_routes()


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
        # for each host in route -> host.forward(Package("data", 0, 1))
        pass


    def show_map(self):
        views.plot_map(self.hosts, WIDTH, HEIGHT)

    
    def reachable_hosts(self, host):
        views.plot_reachable_hosts(self.hosts)


Manager()