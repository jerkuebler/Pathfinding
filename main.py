# Meant to demonstrate a simple pathfinding algorithm with recursion

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
start_node = grid.nodes[0]
visited_nodes = [grid.nodes[0]]

while not done:
    pygame.display.update()
    for node in grid.nodes:
        node.update()

    for path in grid.paths:
        path.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if len(visited_nodes) < len(grid.nodes):
        start_node, visited_nodes = grid.traverse(start_node, visited_nodes)

    clock.tick(1)
