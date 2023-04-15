
from itertools import count
from typing import Iterator


def floors(directions: str) -> Iterator[int]:
    floor = 0
    yield floor
    for char in directions:
        floor += 1 if char == '(' else -1
        yield floor


def first_position_to_enter_basement(directions: str) -> int:
    return next(filter(lambda p: p[0] < 0, zip(floors(directions), count())))[1]


with open('input.txt') as f:
    inputs = f.read().splitlines(keepends=False)

for input in inputs:
    print(first_position_to_enter_basement(input))
