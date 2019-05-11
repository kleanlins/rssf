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
        
    plt.show()


def plot_route(hosts):
    '''
    Gets a list of hosts and plot a route based on first and last objects.
    '''
    pass


def plot_host_routes(host):
    '''
    Plot all possible routes based on a host list of adjacency.
    '''
    pass


def plot_reachable_hosts(host, width, height):
    '''
    Plot an arrow indicating all reachable hosts.
    '''