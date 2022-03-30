import random

from EdgeGraph import EdgeGraph
from MatrixImage import MatrixImage
from MazeEnvironment import MazeEnvironment
from MazeMonitor import MazeMonitor
from utils import initialize_grid_graph, generate_maze

import matplotlib.pyplot as plt


def graph_basic_test():
    graph = EdgeGraph(10)
    print(graph)

    graph.add_node(2)
    print(graph)


def test_grid_graph():
    graph = initialize_grid_graph(4, 3)
    print(graph)

    for number, edge in graph.edges.items():
        print(number, edge)

    print(graph.edge_list)


def test_maze_generator():
    maze, _ = generate_maze(10, 10)
    print(maze)


def test_matrix_image():
    image = MatrixImage(10, 12)

    plt.imshow(image.image)
    plt.show()

    plt.imshow(image.image)
    plt.pause(.001)
    for i in range(10):
        for j in range(12):
            print(i, j)
            image.fill(i, j, (0, 1, 1))
            plt.imshow(image.image)
            plt.pause(.001)
    plt.show()


def test_matrix_image_tools():
    image = MatrixImage(5, 5, background=.5)

    image.fill_upper_edge(1, 1, (1, 0, 1))
    image.fill_lower_edge(1, 1, (1, 1, 0))
    image.fill_upper_edge(1, 2, (1, 0, 1))

    image.fill_left_edge(2, 1, (0, 1, 1))
    image.fill_right_edge(2, 1, (0, 0, 1))

    image.fill_upper_edge(3, 3, .8)
    image.fill_lower_edge(3, 3, .8)
    image.fill_right_edge(3, 3, .8)
    image.fill_left_edge(3, 3, .8)

    image.fill_inside(3, 3, (1, .5, .6))

    image.fill(2, 3, .4)
    image.fill(3, 2, .4)
    image.fill(3, 4, .4)
    image.fill(4, 3, .4)

    fig = plt.gca()

    x_axis = fig.axes.get_xaxis()
    x_axis.set_visible(False)

    y_axis = fig.axes.get_yaxis()
    y_axis.set_visible(False)
    plt.imshow(image.image)
    plt.show()


def test_maze_monitor():
    width = 20
    height = 20
    maze, paths = generate_maze(width, height)
    # print(paths)
    monitor = MazeMonitor(width, height, paths)
    # print(maze)

    fig = plt.gca()

    x_axis = fig.axes.get_xaxis()
    x_axis.set_visible(False)

    y_axis = fig.axes.get_yaxis()
    y_axis.set_visible(False)

    plt.imshow(monitor.image)
    plt.show()

    monitor.move_agent((1, 1))
    plt.imshow(monitor.image)
    plt.show()


def test_maze_env():
    fig = plt.gca()

    x_axis = fig.axes.get_xaxis()
    x_axis.set_visible(False)

    y_axis = fig.axes.get_yaxis()
    y_axis.set_visible(False)

    env = MazeEnvironment(5, 5)
    env.reset()
    state = env.state

    plt.imshow(state)
    plt.pause(0.01)

    for _ in range(100):
        action = random.randint(0, 4)
        print(action)
        reward, state, done, _ = env.step(action)
        print(reward)
        plt.imshow(state)
        plt.pause(0.001)
    plt.show()


if __name__ == '__main__':
    random.seed(100)
    # graph_basic_test()
    # test_grid_graph()
    # test_maze_generator()
    # test_matrix_image()
    # test_matrix_image_tools()
    # test_maze_monitor()
    test_maze_env()
