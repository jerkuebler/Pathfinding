import random
import pygame
from math import sqrt


class Node(pygame.sprite.Sprite):
    def __init__(self, parent, x, y, num):

        pygame.sprite.Sprite.__init__(self)
        self.color = (0, 0, 255)
        self.x = x
        self.y = y
        self.grid = parent
        self.adjacent_nodes = []
        self.num = num

    def update(self):
        pygame.draw.circle(self.grid.screen, self.color, (self.x, self.y), 10, 0)

    def __eq__(self, other):
        if type(other) is type(self):
            if other.x == self.x and other.y == self.y:
                return True
            else:
                return False

    def __repr__(self):
        return "(x:%d, y:%d, num:%d)" % (self.x, self.y, self.num)

    def __str__(self):
        return "(x:%d, y:%d, num:%d)" % (self.x, self.y, self.num)

    def neighbors(self):

        path_list = []
        for o in self.grid.nodes:
            if o != self:
                path_list.append(Path(self.grid.screen, self, o))

        # sorted_paths = sorted(path_list, key=lambda x: x.dist_tot)

        self.adjacent_nodes = path_list

        return self.adjacent_nodes


class Path(pygame.sprite.Sprite):
    def __init__(self, screen, start, finish):

        pygame.sprite.Sprite.__init__(self)

        self.active = True
        self.screen = screen
        self.color = (100, 100, 100)
        self.width = 1
        self.start_node = start
        self.finish_node = finish
        self.dist_x = abs(finish.x - start.x)
        self.dist_y = abs(finish.x - start.x)
        self.dist_tot = sqrt(self.dist_x ** 2 + self.dist_y ** 2)

    def update(self):
        if self.active:
            pygame.draw.line(self.screen, self.color, (self.start_node.x, self.start_node.y),
                             (self.finish_node.x, self.finish_node.y), self.width)

    def __repr__(self):
        return "(start node:(%d,%d), finish node:(%d,%d))" % (self.start_node.x, self.start_node.y,
                                                              self.finish_node.x, self.finish_node.y)

    def __str__(self):
        return "(start node:(%d,%d), finish node:(%d,%d))" % (self.start_node.x, self.start_node.y,
                                                              self.finish_node.x, self.finish_node.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if type(other) is type(self):
            same_start = self.start_node == other.start_node
            same_finish = self.finish_node == other.finish_node
            start_is_finish = self.start_node == other.finish_node
            finish_is_start = self.finish_node == other.start_node
            if same_start and same_finish:
                return True
            elif start_is_finish and finish_is_start:
                return True
            else:
                return False


class Grid():
    def __init__(self):
        self.nodes = []
        self.paths = []
        self.screen = pygame.display.set_mode((640, 480))
        self.traverse_distance = 0
        for x in range(10):
            o = Node(self, random.randint(100, 600), random.randint(100, 400), x)
            self.nodes.append(o)

        for node in self.nodes:
            paths = node.neighbors()
            for path in paths:
                self.paths.append(path)

    def traverse(self, start, visited_nodes):

        green = (0, 255, 0)
        path_distance = 1000
        next_start = None
        chosen_path = None

        for path in start.adjacent_nodes:
            if path.dist_tot < path_distance and path.finish_node not in visited_nodes:
                path_distance = path.dist_tot
                next_start = path.finish_node
                chosen_path = path

        self.traverse_distance += path_distance
        visited_nodes.append(start)
        chosen_path.active = True
        chosen_path.color = green
        chosen_path.width = 5
        print(chosen_path)
        next_start.color = green
        if len(visited_nodes) == len(self.nodes):
            print(self.traverse_distance)

        return next_start, visited_nodes
