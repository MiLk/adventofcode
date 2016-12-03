import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    (a, b, c) = filter(None, line.strip().split(' '))
    return (int(a), int(b), int(c))


def extract_triangles(lines, step):
    if step == 1:
        return [process_line(line) for line in lines]
    else:
        lenghts = {'a': [], 'b': [], 'c': []}
        for line in lines:
            (a, b, c) = process_line(line)
            lenghts['a'].append(a)
            lenghts['b'].append(b)
            lenghts['c'].append(c)
        flat = lenghts['a'] + lenghts['b'] + lenghts['c']
        triangles = []
        for i in xrange(0, len(flat), 3):
            triangles.append((flat[i], flat[i+1], flat[i+2]))
        return triangles


def is_valid_triangle(triangle):
    (a, b, c) = triangle
    return a < b + c and b < a + c and c < a + b


def main():
    lines = readinput(sys.argv[1])

    triangles = extract_triangles(lines, 1)
    count = 0
    for triangle in triangles:
        if is_valid_triangle(triangle):
            count += 1

    print('Step 1: %s' % count)

    triangles = extract_triangles(lines, 2)
    count = 0
    for triangle in triangles:
        if is_valid_triangle(triangle):
            count += 1

    print('Step 2: %s' % count)


if __name__ == "__main__":
    main()
