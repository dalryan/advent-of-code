"""Is it even legal to use a library?"""

import networkx


def read_list_from_file(file_path: str) -> (list[int], list[int]):
    """Ugly, but read the file and split separately into order and sequence"""
    orders, sequences = [], []
    with open(file_path, "r") as f:
        for line in f.read().splitlines():
            if "|" in line:
                orders.append(tuple([int(x) for x in line.strip().split("|")]))
            elif line != "":
                sequences.append([int(x) for x in line.strip().split(",")])
    return orders, sequences


def part_one(order: list[int], sequence: list[int]) -> int:
    """Create a directed graph, topologically sort it, grab the middle
    Only grab the middle if the ordering was correct
    """
    graph = networkx.DiGraph(
        (x, y) for x, y in order if x in sequence and y in sequence
    )
    sorted_list = list(networkx.topological_sort(graph))
    return sorted_list[len(sorted_list) // 2] if sorted_list == sequence else 0


def part_two(order: list[int], sequence: list[int]) -> int:
    """Create a directed graph, topologically sort it, grab the middle
    Only grab the middle if the ordering was incorrect
    """
    graph = networkx.DiGraph(
        (x, y) for x, y in order if x in sequence and y in sequence
    )
    sorted_list = list(networkx.topological_sort(graph))
    return sorted_list[len(sorted_list) // 2] if sorted_list != sequence else 0


ordering, sequences = read_list_from_file("../test.txt")
assert (sum(part_one(ordering, s) for s in sequences)) == 143
assert (sum(part_two(ordering, s) for s in sequences)) == 123
