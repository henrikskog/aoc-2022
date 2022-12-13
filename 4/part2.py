import pprint


def p(args):
    pprint.pprint(args)


def read_input(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f.readlines()]


def transform_input(lines):
    return [
        [
            {'start': int(y.split('-')[0]), 'end': int(y.split('-')[1]),
             'length': int(y.split('-')[1]) - int(y.split('-')[0])}
            for y in x.split(',')]
        for x in lines]


def main():
    data = transform_input(read_input('data.txt'))
    tot = 0
    for pair in data:
        a = pair[0]
        b = pair[1]

        first, last = (a,b) if (a['start'] <= b['start']) else (b,a)

        if last['start'] <= first['end']:
            tot += 1
            continue

    p(tot)


main()
