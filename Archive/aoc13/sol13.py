"""Solution to Day 13 of the 2022 Advent of Code."""

import json
from functools import cmp_to_key
from sys import argv
from typing import Final, Literal

from rich.console import Console


def _compare(left: list[int] | int, right: list[int] | int) -> Literal[-1, 0, 1]:
    """Compare two objects. Return -1, 0, 1 if <, ==, > applies to left ? right, resp."""
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    if isinstance(left, list) and isinstance(right, list):
        left_len = len(left)
        right_len = len(right)
        min_len = min(left_len, right_len)
        for left_item, right_item in zip(left[:min_len], right[:min_len]):
            if (c := _compare(left_item, right_item)) != 0:
                return c
        if left_len < right_len:
            return -1
        elif left_len == right_len:
            return 0
        else:
            return 1
    if isinstance(left, int) and isinstance(right, list):
        return _compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return _compare(left, [right])
    else:
        if isinstance(left, int | list):
            bad = left
        else:
            bad = right
        raise TypeError(
            f"{bad!r} has type {type(bad)}, instead of expected list or int."
        )


def compare(left: list[int] | int, right: list[int] | int) -> bool:
    """Compare left and right, and return True iff left, right are in "right order"."""
    return _compare(left, right) != 1


def compare_strings(left: str, right: str) -> bool:
    """Compare string representations of lists."""
    return compare(json.loads(left), json.loads(right))


def parse_input(text: str) -> list[tuple[str, str]]:
    """Parse the input file and return a list of string tuples."""
    lines = [k for line in text.splitlines() if (k := line.strip())]
    if len(lines) % 2:
        raise ValueError("Odd number of lists.")
    else:
        return [(lines[2 * k], lines[2 * k + 1]) for k in range(0, len(lines) // 2)]


def part1(pairs: list[tuple[str, str]]) -> int:
    """Return the solution of part 1 of the puzzle given the output of parse_input."""
    return sum(idx + 1 for idx, p in enumerate(pairs) if compare_strings(*p))


DIVIDER_PACKETS: Final[list[list[list[int]]]] = [[[2]], [[6]]]


def part2_setup(provided: list[tuple[str, str]]) -> list[list]:
    """Return a list of packets based on the output of parse_input and the dividers."""
    return [json.loads(k) for pair in provided for k in pair] + DIVIDER_PACKETS


def part2(provided: list[tuple[str, str]]) -> int:
    """Return the solution of part 2 of the puzzle given the output of parse_input."""
    packets_in_order = sorted(part2_setup(provided), key=cmp_to_key(_compare))
    output = 1
    for idx, item in enumerate(packets_in_order):
        if any(item == dp for dp in DIVIDER_PACKETS):
            output *= idx + 1
    return output


if __name__ == "__main__":
    c = Console()
    if len(argv) == 1:
        c.print(f"[white on red]Usage:[/] [yellow on black]{argv[0]}[/] filename")
    else:
        with open(argv[1], "rt") as infile:
            raw_text = infile.read()
        parsed = parse_input(raw_text)
        part1_result = part1(parsed)
        c.print(f"[black on light_green]Part 1:[/] [yellow on black]{part1_result}[/]")
        part2_result = part2(parsed)
        c.print(f"[black on light_green]Part 2:[/] [yellow on black]{part2_result}[/]")