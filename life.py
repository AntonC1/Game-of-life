import pygame
from random import randint
from copy import deepcopy

# board size
board = widith, height = 1500, 1000
tile = 25
w, h = widith // tile, height // tile

# picking pattern for our game of life from 6 patterns
pick_pattern = int(input("Pick number from 1 to 6 to pick one of the simulations :"))
if pick_pattern not in range(1, 6):
    pick_pattern = int(input("Error!! Pick number from 1 to 6 to pick one of the simulations :"))
next_pattern = [[0 for i in range(w)] for j in range(h)]

if pick_pattern == 1:
    population_pattern = [[1 if i == w // 2 or j == h // 2 else 0 for i in range(w)] for j in range(h)]
elif pick_pattern == 2:
    population_pattern = [[randint(0, 1) for i in range(w)] for j in range(h)]
elif pick_pattern == 3:
    population_pattern = [[1 if not i % 9 else 0 for i in range(w)] for j in range(h)]
elif pick_pattern == 4:
    population_pattern = [[1 if not (2 * i + j) % 4 else 0 for i in range(w)] for j in range(h)]
elif pick_pattern == 5:
    population_pattern = [[1 if not i % 7 else randint(0, 1) for i in range(w)] for j in range(h)]
elif pick_pattern == 6:
    population_pattern = [[1 if not (i * j) % 22 else 0 for i in range(w)] for j in range(h)]

# time of our life cycles
FPS = int(input("give us time of one life cycles(best is 5 to 10 more is faster) :"))
clock = pygame.time.Clock()
# launching a window with simulation
pygame.init()
surface = pygame.display.set_mode(board)


def check_cell(population_pattern, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if population_pattern[j][i]:
                count += 1

    if population_pattern[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, height)) for x in range(0, widith, tile)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (widith, y)) for y in range(0, height, tile)]
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if population_pattern[y][x]:
                pygame.draw.rect(surface, pygame.Color('blue'), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
            next_pattern[y][x] = check_cell(population_pattern, x, y)

    population_pattern = deepcopy(next_pattern)
    pygame.display.flip()
    clock.tick(FPS)
