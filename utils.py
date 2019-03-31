import random 

def generate_map(hosts, size):

    MAP = [["-" for i in range(size)] for j in range(size)]

    for _ in range(hosts):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        MAP[x][y] = "O"
        print(f"X:{x}\tY:{y}")

    for row in MAP:
        for column in row:
            print(column, end=' ')
        print()