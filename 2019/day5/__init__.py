from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def p1(lines):
    computer = Computer(lines[0])
    computer.input = 1
    computer.run_mode()
    return computer.output


def p2(lines):
    computer = Computer(lines[0])
    computer.input = 5
    computer.run_mode()
    return computer.output
