[Puzzle](https://adventofcode.com/2023/day/1)

# Solution
The first part is straightforward and can be solved a few ways.

For the python solution I chose to iterate over the list and just return the first/last.
This is easily accomplished in python as we can duck type our way to the values.

The second part is quite hard, especially for day 1.

It can probably be solved in a brute-force way:
- remove all digits from the string
- find/replace all number-words with their matching number
- use the functions from part one

It can also be solved with regex, this is maybe the obvious solution.

I have chosen to solve it with a trie, for a few reasons.
1. It's thematic
2. I dislike regex
3. It is a reasonable-enough use case for prefix-trees