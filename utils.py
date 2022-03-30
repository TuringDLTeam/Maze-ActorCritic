import random

from EdgeGraph import EdgeGraph
import numpy as np


def initialize_grid_graph(width, height):
    count = width * height

    graph = EdgeGraph(count)

    for head in range(count):
        for tail in range(head + 1, count):
            # print(head, tail)
            head_y, head_x = divmod(head, width)
            tail_y, tail_x = divmod(tail, width)

            if (head_x - tail_x == 1 and head_y == tail_y) or \
                    (head_x - tail_x == -1 and head_y == tail_y) or \
                    (head_x == tail_x and head_y - tail_y == 1) or \
                    (head_x == tail_x and head_y - tail_y == -1):
                graph.add_edge(head, tail)

    return graph


def merge_sets(set_list, first, second):
    first_index, second_index = -1, -1

    for index, s in enumerate(set_list):
        if first in s:
            first_index = index
        if second in s:
            second_index = index

    if first_index != second_index:
        s1 = set_list[first_index]
        s2 = set_list[second_index]

        set_list.remove(s1)
        set_list.remove(s2)

        set_list.append(s1.union(s2))

        return True

    return False


def get_final_graph(edges, removed_edges):
    answer = []
    complement = []

    for index, edge in enumerate(edges):
        if index in removed_edges:
            answer.append(edge)
        else:
            complement.append(edge)

    return answer, complement


def generate_maze(width, height):
    graph = initialize_grid_graph(width, height)
    sets = [{i} for i in range(width * height)]

    edges = graph.edge_list
    random.shuffle(edges)
    removes_edges = []

    for index, (head, tail) in enumerate(edges):
        if merge_sets(sets, head, tail):
            removes_edges.append(index)

    return get_final_graph(edges, removes_edges)
