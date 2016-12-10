import sys
import re


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def main():
    lines = readinput(sys.argv[1])

    init_lines = [line.strip() for line in lines
                  if line.startswith('value')]
    instruction_lines = [line.strip() for line in lines
                         if line.startswith('bot')]

    bots = {}
    for line in init_lines:
        m = re.match('^value (\d+) goes to bot (\d+)', line)
        value, bot = m.groups()
        if bot not in bots:
            bots[bot] = set()
        bots[bot].add(value)

    instructions = {}
    for line in instruction_lines:
        m = re.match('bot (\d+) gives low to (\w+) (\d+)'
                     ' and high to (\w+) (\d+)', line)
        bot, ldest, lnum, hdest, hnum = m.groups()
        instructions[bot] = (ldest, lnum, hdest, hnum)

    outputs = {'0': set(), '1': set(), '2': set()}
    to_process = True
    while to_process:
        to_process = [k for (k, v) in bots.iteritems() if len(v) >= 2]
        for bot in to_process:
            h = bots[bot].pop()
            l = bots[bot].pop()
            if int(l) > int(h):
                l, h = h, l
            if h == '61' and l == '17':
                print('Step 1: %s' % bot)
            ldest, lnum, hdest, hnum = instructions[bot]
            if ldest == 'bot':
                if lnum not in bots:
                    bots[lnum] = set()
                bots[lnum].add(l)
            else:
                if lnum in outputs:
                    outputs[lnum].add(l)
            if hdest == 'bot':
                if hnum not in bots:
                    bots[hnum] = set()
                bots[hnum].add(h)
            else:
                if hnum in outputs:
                    outputs[hnum].add(h)

    a, b, c = [int(outputs[str(i)].pop()) for i in xrange(0, 3)]
    print('Step 2: %d' % (a * b * c))


if __name__ == "__main__":
    main()
