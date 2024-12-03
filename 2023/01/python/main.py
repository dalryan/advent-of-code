import trie


def read_list_from_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def get_first_int(s: str) -> int:
    for i in s:
        try:
            return int(i)
        except ValueError:
            continue


def get_last_int(s: str) -> int:
    for i in reversed(s):
        try:
            return int(i)
        except ValueError:
            continue


def part1(lst: list[str]) -> int:
    total = 0
    for row in lst:
        total += int(f"{get_first_int(row)}{get_last_int(row)}")
    return total


def part2(lines: list[str]) -> int:
    number_finder = trie.ChristmasTrie()
    total = 0

    for line in lines:
        numbers = number_finder.find_numbers(line)

        if numbers:
            first_digit = numbers[0][1]
            last_digit = numbers[-1][1]
            value = int(first_digit + last_digit)
            total += value

    return total


if __name__ == "__main__":
    data = read_list_from_file("../test1.txt")
    assert part1(data) == 142
    data = read_list_from_file("../test2.txt")
    assert part2(data) == 281
