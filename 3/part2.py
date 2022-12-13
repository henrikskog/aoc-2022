import pprint

def p(args):
    pprint.pprint(args)


# Read data from data.txt
def get_priority(letter: str) -> int:
    # If letter is lower case
    if ord(letter) >= 97:
        return ord(letter) - 96

    return ord(letter) - 64 + 26

def read_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def transform_input(lines):
    result = []
    for x in range((len(lines) // 3)):
        result.append(
            [
                lines[x*3].strip(),
                lines[x*3+1].strip(),
                lines[x*3+2].strip(),
            ]
        )

    return result

def get_common(str1, str2, str3) -> str:
    for i in str1:
        if i in str2:
            if i in str3:
                return i
    raise Exception("No common found")

def get_score(str) -> int:
    score = 0
    for letter in str:
        score += get_priority(letter)
    return score

def main():
    lines = transform_input(read_input('data.txt'))
    score = 0

    for group in lines:
        common = get_common(group[0], group[1], group[2])
        score += get_score(common)
        print("For the list {} and {}, the common is {} and the score is {}".format(group[0], group[1], common, get_score(common)))

    print(score)


main()
