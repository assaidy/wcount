#!/usr/bin/env python3

import string
import sys
from collections import defaultdict


def read_entire_file_words(file_path: str) -> dict[str, int]:
    words_to_count: dict[str, int] = defaultdict(int)
    with open(file_path, "r") as file:
        word = ""
        while ch := file.read(1):
            if ch.isspace():
                if word:
                    words_to_count[clean_word(word)] += 1
                    word = ""
                continue
            word += ch
    return words_to_count


def clean_word(word: str, remove_digits: bool = False) -> str:
    to_remove: str = string.punctuation + string.whitespace
    if remove_digits:
        to_remove += string.digits
    return word.strip(to_remove).lower()


if __name__ == "__main__":
    program: str = sys.argv[0]
    if len(sys.argv) < 2:
        print("ERROR: not enough files to process were provided")
        print(f"Usage: {program} <FILE_PATH>")
        sys.exit(1)

    file_path: str = sys.argv[1]

    ALL_UNIQUE_WORDS: list[tuple[str, int]] = sorted(
        read_entire_file_words(file_path).items(), key=lambda x: x[1], reverse=True
    )
    ALL_UNIQUE_WORDS_COUNT: int = len(ALL_UNIQUE_WORDS)

    for word, count in ALL_UNIQUE_WORDS[-100:]:
        print(f"{word:<20} => {count}")
    print(f"\n==> {ALL_UNIQUE_WORDS_COUNT=}")
