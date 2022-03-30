from Environment import Environment
from MazeMonitor import MazeMonitor
from VertexGraph import VertexGraph
from utils import generate_maze


class MazeEnvironment(Environment):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        paths, walls = generate_maze(width, height)
        self.__monitor = MazeMonitor(width, height, walls)

        self.__position = (0, 0)
        self.__goal_position = (self.__width - 1, self.__height - 1)
        self.__transition_graph = VertexGraph.from_edge_graph(paths, self.__width * self.__height)

    @property
    def state(self):
        return self.__monitor.image

    def reset(self):
        paths, walls = generate_maze(self.__width, self.__height)
        self.__monitor = MazeMonitor(self.__width, self.__height, walls)
        self.__position = (0, 0)
        self.__monitor.move_agent(self.__position)

        self.__transition_graph = VertexGraph.from_edge_graph(paths, self.__width * self.__height)

    def __get_node_index(self, x, y):
        return y * self.__width + x

    def __get_new_position(self, action):
        current_x, current_y = self.__position
        current_index = self.__get_node_index(*self.__position)
        new_x, new_y = current_x, current_y

        if action == 0:  # Up
            new_y = max(0, current_y - 1)
        elif action == 1:  # Down
            new_y = min(self.__width - 1, current_y + 1)
        elif action == 2:  # Right
            new_x = min(self.__height - 1, current_x + 1)
        elif action == 3:  # Left
            new_x = max(0, current_x - 1)

        new_index = self.__get_node_index(new_x, new_y)

        if self.__transition_graph.are_adjacent(current_index, new_index):
            return new_x, new_y
        
        return current_x, current_y

    def step(self, action):
        new_pos = self.__get_new_position(action)
        # print(new_pos)
        self.__position = new_pos
        self.__monitor.move_agent(new_pos)

        if new_pos == self.__goal_position:
            return 100, self.__monitor.image, True, None

        return -1, self.__monitor.image, False, None

    def end(self):
        pass
