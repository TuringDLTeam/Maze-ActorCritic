from MatrixImage import MatrixImage


class MazeMonitor:
    BACKGROUND = .7
    WALL = .2
    AGENT = (.9, .5, .2)

    def __init__(self, width, height, walls):
        self.__image = MatrixImage(width, height, background=MazeMonitor.BACKGROUND, edge_thickness=1)
        self.__width = width
        self.__height = height

        self.__add_walls(walls)
        self.__add_borders()

        self.__agent_pos = (0, 0)
        self.__image.fill_inside(0, 0, MazeMonitor.AGENT)

    def __add_borders(self):
        for i in range(self.__width):
            self.__image.fill_upper_edge(i, 0, MazeMonitor.WALL)
            self.__image.fill_lower_edge(i, self.__height - 1, MazeMonitor.WALL)

        for i in range(self.__height):
            self.__image.fill_left_edge(0, i, MazeMonitor.WALL)
            self.__image.fill_right_edge(self.__width - 1, i, MazeMonitor.WALL)

        self.__image.fill_left_edge(0, 0, MazeMonitor.BACKGROUND)
        self.__image.fill_right_edge(self.__width - 1, self.__height - 1, MazeMonitor.BACKGROUND)

    def __add_walls(self, graph):
        for edge in graph:
            first, second = edge

            first_y, first_x = divmod(first, self.__width)
            second_y, second_x = divmod(second, self.__width)

            if first_x == second_x:
                if first_y < second_y:
                    self.__image.fill_lower_edge(first_x, first_y, MazeMonitor.WALL)
                    self.__image.fill_upper_edge(second_x, second_y, MazeMonitor.WALL)
                else:
                    self.__image.fill_upper_edge(second_x, second_y, MazeMonitor.WALL)
                    self.__image.fill_lower_edge(first_x, first_y, MazeMonitor.WALL)
            else:
                if first_x < second_x:
                    self.__image.fill_right_edge(first_x, first_y, MazeMonitor.WALL)
                    self.__image.fill_left_edge(second_x, second_y, MazeMonitor.WALL)
                else:
                    self.__image.fill_left_edge(second_x, second_y, MazeMonitor.WALL)
                    self.__image.fill_right_edge(first_x, first_y, MazeMonitor.WALL)

    def move_agent(self, new_pos):
        x, y = new_pos
        self.__image.fill_inside(*self.__agent_pos, MazeMonitor.BACKGROUND)
        self.__image.fill_inside(x, y, MazeMonitor.AGENT)
        self.__agent_pos = new_pos

    @property
    def image(self):
        return self.__image.image
