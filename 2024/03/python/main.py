import re


def read_str_from_file(file_path: str) -> str:
    """Just read a string from a file."""
    with open(file_path, "r") as f:
        return f.read()


def part_one(s: str) -> int:
    """It's regex time"""
    pattern = r"mul\((\d+),(\d+)\)"
    return sum([int(a) * int(b) for a, b in re.findall(pattern, s)])


def part_two(s: str) -> int:
    """It's still regex time"""
    values = []
    pattern = r"(mul|don't|do\b)(?:\((\d+),(\d+)\))?"
    active = True
    for smt in re.findall(pattern, s):
        # goofin' around
        active = False if smt[0] == "don't" else (active or smt[0] == "do")
        if not active:
            continue
        try:
            values.append(int(smt[1]) * int(smt[2]))
        except ValueError:
            continue
    return sum(values)


if __name__ == "__main__":
    data = read_str_from_file("../test.txt")
    assert part_one(data) == 161
    assert part_two(data) == 48
