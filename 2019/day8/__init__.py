from collections import Counter

from utils import str_lines

parse_input = str_lines


def p1(lines):
    image_raw = lines[0]
    layer_size = 25 * 6
    counters = {
        i: Counter(image_raw[i * layer_size: (i + 1) * layer_size])
        for i in range(len(image_raw) // layer_size)
    }
    return min((
        (c['0'], c['1'] * c['2'])
        for i, c in counters.items()
    ), key=lambda x: x[0])[1]


def p2(lines):
    image_raw = lines[0]
    w, h = 25, 6
    layer_size = w * h
    layers = len(image_raw) // layer_size

    def visible(x, y):
        return next(
            p for l in range(layers)
            if (p := image_raw[l * layer_size + y * w + x]) != '2'
        )

    print('\n'.join([
        ''.join(['█' if visible(x, y) == '0' else ' ' for x in range(w)])
        for y in range(h)
    ]))
