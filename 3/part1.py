# Read data from data.txt

def get_priority(letter: str) -> int:
    # If letter is lower case
    if ord(letter) >= 97:
        return ord(letter) - 96

    return ord(letter) - 64 + 26

def read_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def get_common(str1, str2) -> str:
    common = ''
    for i in str1:
        if i in str2:
            common = i
    return common

def get_score(str) -> int:
    score = 0
    for letter in str:
        score += get_priority(letter)
    return score

def main():
    lines = read_input('data.txt')
    score = 0

    for line in lines:
        rs1 = line[:(len(line) // 2)]
        rs2 = line[(len(line) // 2):]

        common = get_common(rs1, rs2)
        score += get_score(common)
        print("For the list {} and {}, the common is {} and the score is {}".format(rs1, rs2, common, get_score(common)))

    print(score)

main()