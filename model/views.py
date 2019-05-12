# THIS FILE CONTAINS ALL METHODS FOR DATA TRANSMITTION PLOTTING AND 
# LOGGING INFORMATION
import matplotlib.pyplot as plt
import math

def plot_map(hosts, width, height):
    '''
    Plot a representation of a map containing all hosts and it's
    aproximate signal range.    
    '''
    # figure dimensions
    plt.axis([0, width, 0, height])

    # figure labels
    plt.xlabel("in Km")
    plt.ylabel("in Km")

    for host in hosts:
        # plotting host representation
        plt.plot(host.position[0], host.position[1], 'k^')
        
        # plotting host name
        plt.annotate(host.address, (host.position[0]+0.1, host.position[1]+0.1))
    
        # plotting estimated area coverage
        area = math.pi * (host.range ** 2)
        plt.scatter(host.position[0], host.position[1], s=area*900, alpha=0.1)
        
    plt.show()


def plot_route(hosts, route, width, height):
    '''
    Gets a list of hosts and plot a route based on first and last objects.
    '''
    # figure dimensions
    plt.axis([0, width, 0, height])
    # fig = plt.figure(figsize = (10,10))

    # figure labels
    plt.xlabel("in Km")
    plt.ylabel("in Km")

    for host in hosts:
        # plotting host representation
        plt.plot(host.position[0], host.position[1], 'k^')
        
        # plotting host name
        plt.annotate(host.address, (host.position[0]+0.1, host.position[1]+0.1))
    
        # plotting estimated area coverage
        area = math.pi * (host.range ** 2)
        plt.scatter(host.position[0], host.position[1], s=area*900, alpha=0.1)
        

    for i in range(len(route)-1):
        x = route[i].position[0]
        y = route[i].position[1]

        dx = route[i+1].position[0] - route[i].position[0]
        dy = route[i+1].position[1] - route[i].position[1]

        # plt.arrow(route[i].position[0], route[i].position[1], route[i+1].position[0], route[i+1].position[1])
        plt.arrow(x, y, dx, dy)


    plt.show()


def plot_host_routes(hosts, origin, width, height):
    '''
    Plot all possible routes based on a host list of adjacency.

        assumindo que vá receber adj_list_A = [B,C,D]
        Desenho fica:
                          B  
                         /
                        A -- C
                         \
                          D
    '''
    # figure dimensions
    plt.axis([0, width, 0, height])
    # fig = plt.figure(figsize = (10,10))

    # figure labels
    plt.xlabel("in Km")
    plt.ylabel("in Km")

    for host in hosts:
        # plotting host representation
        plt.plot(host.position[0], host.position[1], 'k^')
        
        # plotting host name
        plt.annotate(host.address, (host.position[0]+0.1, host.position[1]+0.1))
    
        # plotting estimated area coverage
        area = math.pi * (host.range ** 2)
        plt.scatter(host.position[0], host.position[1], s=area*900, alpha=0.1)
    
    for i in range(len(origin.adj)-1):
        x = hosts[origin].position[0]
        y = hosts[origin].position[1]

        dx = hosts[origin].adj[i+1].position[0] - hosts[origin].position[0]
        dy = hosts[origin].adj[i+1].position[1] - hosts[origin].position[1]
        
        plt.arrow(x, y, dx, dy)

    plt.show()


def plot_reachable_hosts(host):
    '''
    Plot an arrow indicating all reachable hosts.
    '''
    