"""Bro, just use a regex..."""

from typing import Optional

MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


class TrieNode:

    def __init__(self):
        self.children: dict = {}
        self.value: Optional[str] = None


class ChristmasTrie:

    def __init__(self):
        self.root: TrieNode = TrieNode()
        self._build_trie()

    def _build_trie(self) -> None:
        for word, value in MAPPING.items():
            self._insert_word(word, value)

    def _insert_word(self, word: str, value: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value

    def find_numbers(self, s: str) -> list[tuple[int, str]]:
        numbers = []
        for i in range(len(s)):
            node = self.root
            cur_i = i
            while cur_i < len(s) and s[cur_i] in node.children:
                node = node.children[s[cur_i]]
                if node.value is not None:
                    numbers.append((i, node.value))
                cur_i += 1
        return numbers
