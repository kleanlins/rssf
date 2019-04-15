import random 

def generate_coordinates(hosts_quantity, width, height):
    '''
    'hosts_quantity' defines how much coordinates will be generated

    'map_size' represents the width and height of a square shaped map 
    '''

    # each position of the arrays below are tied together to form a host coordinate
    x_positions = list()
    y_positions = list()

    for _ in range(hosts_quantity):
        x = random.randint(0, width-1)
        x_positions.append(x)

        y = random.randint(0, height-1)
        y_positions.append(y)

        # print(f"Generated a host with position: [{x},{y}]")

    return x_positions, y_positions