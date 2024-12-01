from collections import Counter


def read_lists_from_file(file_path: str) -> (list, list):
    """Read the input file and parse the values into lists

    :param file_path: string path to the file
    :return: a tuple of lists
    """
    with open(file_path, "r") as file:
        lines = [line.strip().split() for line in file]

    left = [int(row[0]) for row in lines]
    right = [int(row[1]) for row in lines]
    return left, right


def part_one(left: list[int], right: list[int]) -> int:
    """Solve part 1 of the problem.

    :param left: list of ints
    :param right: list of ints
    :return: sum of the corresponding list values
    """
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part_two(left: list[int], right: list[int]) -> int:
    """Solve part 2 of the problem.

    :param left: list of ints
    :param right: list of ints
    :return: sum of the occurrences
    """
    return sum(num * count for num, count in (Counter(right)).items() if num in left)


if __name__ == "__main__":
    left_list, right_list = read_lists_from_file("2024/01/data.txt")
    assert part_one(left_list, right_list) == 3574690
    assert part_two(left_list, right_list) == 22565391
