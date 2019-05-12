# models
from router import Router
from host import Host

# utils
import utils
import views

# __init__ variables
WIDTH = 15
HEIGHT = 15

HOSTS_QUANTITY = 15
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
        print(f"\nGen {HOSTS_QUANTITY} hosts in {WIDTH}x{HEIGHT} Km...", end=" ")
        positions = utils.generate_coordinates(HOSTS_QUANTITY, WIDTH, HEIGHT)
        for position in positions:
            self.hosts.append(Host(position, SIGNAL_RANGE))
        print(f"{HOSTS_QUANTITY} hosts were created.")

        ## ROUTER INSTANTIATION ##
        print("Creating router...", end=" ")
        self.router = Router(self.hosts)
        print("Router created.")

        # gives an list of near active hosts for each host
        print("Running Hello for each host...", end=" ")
        self.router.hello()
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

    
    def reachable_hosts(self, host_id):
        views.plot_reachable_hosts(self.hosts[host_id], WIDTH, HEIGHT)


    def find_routes(self, id):
        for i in range(len(self.hosts)):
            if i != id:
                self.router.create_routes(id, i)


    def show_routes(self, host_id):
        print(self.hosts[host_id].routes)


    def show_route(self, host_id, host_dest):
        route, _ = self.hosts[host_id].routes[host_dest]
        views.plot_route(self.hosts, route, WIDTH, HEIGHT)


    def set_offline(self, host_id):
        '''
        Sets an host to offline status.
        '''

        self.hosts[host_id].change_status()
        self.find_routes(host_id)

        # find_routes again
        pass


m = Manager()
m.show_map()