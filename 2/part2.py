import sys
from enum import Enum

class Result(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0

# Opponents first, then the points are determined what you play in response
rules = {
    'A': {
        'A': Result.DRAW,
        'B': Result.WIN,
        'C': Result.LOOSE,
    },
    'B': {
        'A': Result.LOOSE,
        'B': Result.DRAW,
        'C': Result.WIN,
    },
    'C': {
        'A': Result.WIN,
        'B': Result.LOOSE,
        'C': Result.DRAW,
    } ,
}

choice_points = {
    'A': 1,
    'B': 2,
    'C': 3,
}

second_column = {
    'X': Result.LOOSE,
    'Y': Result.DRAW,
    'Z': Result.WIN,
}

total_points = 0
for line in sys.stdin.readlines():
    line = line.strip().split(" ")
    opponent = line[0]
    goal = second_column[line[1]]

    options = rules[opponent]

    for key, value in options.items():
        if value == goal:
            total_points += choice_points[key] + value.value

print(total_points)