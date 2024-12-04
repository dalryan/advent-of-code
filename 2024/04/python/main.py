def read_list_from_file(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


def find_pattern(x: int, y: int, dx: int, dy: int):
    """Check if we can find the target string in any direction

    :param x: x coordinate
    :param y: y coordinate
    :param dx: x direction
    :param dy: y direction
    :return: bool
    """
    if not (0 <= x + 3 * dx < len(data) and 0 <= y + 3 * dy < len(data[0])):
        return False
    return all(data[x + i * dx][y + i * dy] == "XMAS"[i] for i in range(4))


def part_one(grid: list[str]):
    """Solve part one

    Iterate over the grid and search for the string in any direction

    :param grid: list of strings
    :return: count of strings found
    """
    total = 0
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for di, dj in directions:
                if find_pattern(i, j, di, dj):
                    total += 1
    return total


def part_two(grid: list[str]):
    """Solve part two

    Iterate over the grid and search for MAS in an X pattern

    :param grid: list of strings
    :return: count of strings found
    """
    count = 0

    def find_pattern_x(x: int, y: int, dx: int, dy: int):
        """Find the pattern in an x shape"""
        if not (0 <= x + 2 * dx < len(grid) and 0 <= y + 2 * dy < len(grid[0])):
            return False
        forwards = (
            grid[x][y] == "M"
            and grid[x + dx][y + dy] == "A"
            and grid[x + 2 * dx][y + 2 * dy] == "S"
        )
        backwards = (
            grid[x][y] == "S"
            and grid[x + dx][y + dy] == "A"
            and grid[x + 2 * dx][y + 2 * dy] == "M"
        )
        return forwards or backwards

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != "A":
                continue
            diagonals = [[(1, 1), (-1, 1)], [(1, -1), (-1, -1)]]
            for d1, d2 in diagonals:
                if (
                    find_pattern_x(i - d1[0], j - d1[1], d1[0], d1[1])
                    or find_pattern_x(i + d1[0], j + d1[1], -d1[0], -d1[1])
                ) and (
                    find_pattern_x(i - d2[0], j - d2[1], d2[0], d2[1])
                    or find_pattern_x(i + d2[0], j + d2[1], -d2[0], -d2[1])
                ):
                    count += 1
    return count // 2


if __name__ == "__main__":
    data = read_list_from_file("../test.txt")
    assert part_one(data) == 18
    assert part_two(data) == 9
