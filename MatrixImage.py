import numpy as np


class MatrixImage:
    def __init__(self, width, height, **kwargs):
        self.__width = width
        self.__height = height

        self.__scale_factor = kwargs.get('scale_factor', 10)
        background = kwargs.get('background', (.1, .1, .1))
        self.__image = np.ones(
            (self.__height * self.__scale_factor, self.__width * self.__scale_factor, 3)) * background

        self.__edge_thickness = kwargs.get('edge_thickness', 2)

    def fill(self, x, y, color):
        start_x = x * self.__scale_factor
        start_y = y * self.__scale_factor
        end_x = start_x + self.__scale_factor
        end_y = start_y + self.__scale_factor

        self.__image[start_y:end_y, start_x:end_x] = color

    def fill_upper_edge(self, x, y, color):
        start_x = x * self.__scale_factor
        start_y = y * self.__scale_factor
        end_x = start_x + self.__scale_factor
        end_y = start_y + self.__edge_thickness

        self.__image[start_y:end_y, start_x:end_x] = color

    def fill_lower_edge(self, x, y, color):
        start_x = x * self.__scale_factor
        start_y = (y + 1) * self.__scale_factor - self.__edge_thickness
        end_x = start_x + self.__scale_factor
        end_y = start_y + self.__edge_thickness

        self.__image[start_y:end_y, start_x:end_x] = color

    def fill_left_edge(self, x, y, color):
        start_x = x * self.__scale_factor
        start_y = y * self.__scale_factor
        end_x = start_x + self.__edge_thickness
        end_y = start_y + self.__scale_factor

        self.__image[start_y:end_y, start_x:end_x] = color

    def fill_right_edge(self, x, y, color):
        start_x = (x + 1) * self.__scale_factor - self.__edge_thickness
        start_y = y * self.__scale_factor
        end_x = start_x + self.__edge_thickness
        end_y = start_y + self.__scale_factor

        self.__image[start_y:end_y, start_x:end_x] = color

    def fill_inside(self, x, y, color):
        start_x = x * self.__scale_factor + self.__edge_thickness
        start_y = y * self.__scale_factor + self.__edge_thickness
        end_x = start_x + self.__scale_factor - 2 * self.__edge_thickness
        end_y = start_y + self.__scale_factor - 2 * self.__edge_thickness

        self.__image[start_y:end_y, start_x:end_x] = color

    @property
    def image(self):
        return self.__image
