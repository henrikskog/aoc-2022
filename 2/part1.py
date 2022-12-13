import sys
from enum import Enum

allSums = []


class Result(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0

# You first, then the points are determined what the opponent plays in response
rules = {
    'A': {
        'A': Result.DRAW,
        'B': Result.LOOSE,
        'C': Result.WIN,
    },
    'B': {
        'A': Result.WIN,
        'B': Result.DRAW,
        'C': Result.LOOSE,
    },
    'C': {
        'A': Result.LOOSE,
        'B': Result.WIN,
        'C': Result.DRAW,
    } ,
}

points = {
    'A': 1,
    'B': 2,
    'C': 3,
}

second_column = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

total_points = 0
for line in sys.stdin.readlines():
    line = line.strip().split(" ")
    opponent = line[0]
    yours = second_column[line[1]]

    total_points += rules[yours][opponent].value + points[yours]

print(total_points)