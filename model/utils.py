import random 

def generate_coordinates(hosts_quantity, width, height):
	'''
	'hosts_quantity' defines how much coordinates will be generated

	'width' and 'height' represents the width and height in Km of a map 
	'''

	# each position of the arrays below are tied together to form a host coordinate

	positions = list()

	for _ in range(hosts_quantity):
		
		x = random.randint(0, width-1)
		y = random.randint(0, height-1)

		position = (x if x != 0 else x+1, y if y != 0 else y+1)

		if position not in positions:
			positions.append(position)

	return positions
