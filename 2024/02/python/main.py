def read_list_from_file(file_path: str) -> list[list[int]]:
    """Read from the file and shove into a nested list of ints"""
    with open(file_path, "r") as f:
        return [list(map(int, line.split())) for line in f.read().splitlines()]


def part_one(lst: list[int]) -> bool:
    """Iterate of the list and check that it fits the safe criteria

    - strictly monotonically increasing OR decreasing
    - difference between ints is 1 <= x <= 3
    """
    inc, dec = [], []
    # there's probably a nicer way to do this
    for i in range(len(lst) - 1):
        inc.append(lst[i] < lst[i + 1])
        dec.append(lst[i] > lst[i + 1])
        diff = abs(lst[i] - lst[i + 1])
        if not (1 <= diff <= 3):
            return False
    return all(inc) or all(dec)


def part_two(lst: list[int]) -> bool:
    """Check for a safe subsequence where 1 value can be removed"""
    if part_one(lst):
        return True

    for i in range(len(lst)):
        left, right = lst[:i], lst[i + 1 :]
        if part_one(left + right):
            return True
    return False


if __name__ == "__main__":
    data = read_list_from_file("../test.txt")
    assert sum(part_one(i) for i in data) == 2
    assert sum(part_two(i) for i in data) == 4
