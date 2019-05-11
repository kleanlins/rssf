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


def plot_route(hosts, width, height)):
    '''
    Gets a list of hosts and plot a route based on first and last objects.
    '''
    # figure dimensions
    plt.axis([0, width, 0, height])

    # figure labels
    plt.xlabel("in Km")
    plt.ylabel("in Km")

    for i in range(hosts):
        if(i<len(hosts)):
            # plotting host representation
            plt.plot(hosts[i].position[0], hosts[i].position[1], 'k^')

            # plotting host name
            plt.annotate(hosts[i].address, (hosts[i].position[0]+0.1, hosts[i].position[1]+0.1))

            # plotting estimated area coverage
            area = math.pi * (hosts[i].range ** 2)
            plt.scatter(hosts[i].position[0], hosts[i].position[1], s=area*900, alpha=0.1)

            # plotting the path from actual host to the next host
            plt.arrow(hosts[i].position[0], hosts[i].position[1], hosts[i+1].position[0] - hosts[i].position[0], hosts[i+1].position[1] - hosts[i].position[1])
    
    plt.show()


def plot_host_routes(host):
    '''
    Plot all possible routes based on a host list of adjacency.
    '''
    pass


def plot_reachable_hosts(host):
    '''
    Plot an arrow indicating all reachable hosts.
    '''
    