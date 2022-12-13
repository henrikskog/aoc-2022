from typing import List, Tuple
from enum import Enum
import ast
import pprint

def compare(left, right):
    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0

# If both values are integers, the lower integer should come first. 
#   If the left integer is lower than the right integer, the inputs are in the right order. 
#   If the left integer is higher than the right integer, the inputs are not in the right order. 
#   Otherwise, the inputs are the same integer; continue checking the next part of the input.
# If both values are lists, compare the first value of each list, then the second value, and so on. 
#   If the left list runs out of items first, the inputs are in the right order. 
#   If the right list runs out of items first, the inputs are not in the right order. 
#   If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. 
#   For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

# Create a variable of type List with integers called left without instantiation, and import the List class from typing

def compare_lists(left: List[int], right: List[int]) -> bool:
    if len(left) == 0:
        return True
    if len(right) == 0:
        return False

    if isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] < right[0]:
            return True
        if left[0] > right[0]:
            return False

    elif isinstance(left[0], list) and isinstance(right[0], list):
        return compare_lists(left[0], right[0])

    elif isinstance(left[0], int):
        return compare_lists([left[0]], right[0])

    elif isinstance(right[0], int):
        return compare_lists(left[0], [right[0]])

    return compare_lists(left[1:], right[1:])

def convert_string_to_list(string):
    root = []
    current = root
    parent = None

    for char in string:
        if char == '[':
            current.append([])
            parent = current
            current = current[-1]
        elif char == ']':
            current = parent
        elif char == ',':
            pass
        else:
            current.append(int(char))
    

    return current

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        result = []
        packet = []
        for line in lines:
            # If line is empty, continue
            if line.strip() == '':
                continue
            packet.append(ast.literal_eval(line))
            if len(packet) == 2:
                result.append(packet)
                packet = []

    return result

def main():
    inputs = read_input('data.txt')
    tot = 0
    for index, input in enumerate(inputs):
        result = compare_lists(input[0], input[1])
        if result:
            print(f'Input {index + 1} is in the right order')
            tot += index + 1

    print(tot)


main()

# print(compare_lists([1,1,3,1,1], [1,1,5,1,1]))
# print(compare_lists([[1],[2,3,4]], [[1],4]))
# print(compare_lists([9], [[8,7,6]]))
# print(compare_lists([[4,4],4,4], [[4,4],4,4,4]))
# print(compare_lists([7,7,7,7], [7,7,7]))
# print(compare_lists([], [3]))
# print(compare_lists([[[]]], [[]]))
# print(compare_lists([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))