import random 

def generate_coordinates(hosts_quantity, width, height):
    '''
    'hosts_quantity' defines how much coordinates will be generated

    'width' and 'height' represents the width and height in Km of a map 
    '''

    # each position of the arrays below are tied together to form a host coordinate
    x_positions = list()
    y_positions = list()

    for _ in range(hosts_quantity):
        
        #For X
        x = random.randint(0, width-1)
        
        if(x == 0):
             x_positions.append(x+1)
        else:
             x_positions.append(x)

        #For Y
        y = random.randint(0, height-1)

        if(y == 0):
             y_positions.append(y+1)
        else:
             y_positions.append(y)

        # print("Generated a host with position: ")
        # print(x,y)

    return x_positions, y_positions