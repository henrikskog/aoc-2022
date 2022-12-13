import pprint

def p(args):
    pprint.pprint(args)

"""Gets and strips the problem input

@returns: a list of strings representing each line of the input
"""
def d():
    with open('data.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]

"""Gets and strips the test input for the problem

@returns: a list of strings representing each line of the input
"""
def td():
    with open('test-input.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]


def transform_input(lines):
    pass


def main():
    data = transform_input(td())
    pass

main()