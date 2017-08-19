import pygame

import grid

pygame.init()
pygame.display.set_caption('Pathfinding')
grid = grid.Grid()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
grid.screen.fill(BLACK)
clock = pygame.time.Clock()
done = False

grid.traverse(grid.nodes[0], [grid.nodes[0]], grid.nodes[9])
print(grid.traverse_distance)

while not done:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for node in grid.nodes:
        node.update()

    for path in grid.paths:
        path.update()

    clock.tick(10000)
