from collections import defaultdict
from dataclasses import dataclass
from typing import List, Callable, Dict, Tuple, Optional


@dataclass
class Instruction:
    parameters: int
    fn: Callable[..., Optional[int]]


class Computer:
    def __init__(self, memory: List[int]):
        self.__memory = defaultdict(int)
        for i, v in enumerate(memory):
            self.__memory[i] = v

        self.__opcodes: Dict[int, Instruction] = {
            1: Instruction(3, self.__add),
            2: Instruction(3, self.__mul),
            3: Instruction(1, self.__save),
            4: Instruction(1, self.__load),
            5: Instruction(2, self.__jtrue),
            6: Instruction(2, self.__jfalse),
            7: Instruction(3, self.__lt),
            8: Instruction(3, self.__eq),
            9: Instruction(1, self.__set_base),
        }

        self.input = None
        self.output = None
        self.relative_base = 0

    def run(self, initialization: List[Tuple[int, int]]) -> int:
        for address, value in initialization:
            self.__memory[address] = value

        ip = 0
        while (opcode := self.__memory[ip]) != 99:
            instruction = self.__opcodes[opcode]
            instruction.fn(*self.__parameters(ip, instruction))
            ip += 1 + instruction.parameters
        return self.__memory[0]

    def run_mode(self):
        ip = 0
        while (opcode_mode := str(self.__memory[ip])) != "99":
            opcode = int(opcode_mode[-2:])
            modes = tuple(int(m) for m in opcode_mode[:-2].zfill(3))
            if not modes:
                modes = (0, 0)
            instruction = self.__opcodes[opcode]
            jump = instruction.fn(*self.__parameters(ip, instruction), modes)
            if jump:
                ip = jump
            else:
                ip += 1 + instruction.parameters
        return self.__memory[0]

    def run_output(self):
        ip = 0
        while (opcode_mode := str(self.__memory[ip])) != "99":
            opcode = int(opcode_mode[-2:])
            modes = tuple(int(m) for m in opcode_mode[:-2].zfill(3))
            if not modes:
                modes = (0, 0)
            instruction = self.__opcodes[opcode]
            jump = instruction.fn(*self.__parameters(ip, instruction), modes)
            if jump:
                ip = jump
            else:
                ip += 1 + instruction.parameters
            if opcode == 4:
                yield self.output
        return None

    def __parameters(self, ip: int, instruction: Instruction):
        return [
            self.__memory[i]
            for i in range(ip + 1, ip + 1 + instruction.parameters)
        ]

    def __value(self, k, m):
        if m == 0:
            return self.__memory[k]
        if m == 1:
            return k
        if m == 2:
            return self.__memory[self.relative_base + k]

    def __add(self, a: int, b: int, c: int, modes=(0, 0)):
        x, y = self.__value(a, modes[-1]), self.__value(b, modes[-2])
        offset = self.relative_base if modes[-3] == 2 else 0
        self.__memory[c + offset] = x + y

    def __mul(self, a: int, b: int, c: int, modes=(0, 0)):
        x, y = self.__value(a, modes[-1]), self.__value(b, modes[-2])
        offset = self.relative_base if modes[-3] == 2 else 0
        self.__memory[c + offset] = x * y

    def __save(self, a: int, modes):
        """
        Opcode 3 takes a single integer as input and saves it to the address given by its only parameter.
        For example, the instruction 3,50 would take an input value and store it at address 50.
        """
        offset = self.relative_base if modes[-1] == 2 else 0
        self.__memory[a + offset] = next(self.input)

    def __load(self, a: int, modes):
        """
        Opcode 4 outputs the value of its only parameter.
        For example, the instruction 4,50 would output the value at address 50.
        """
        self.output = self.__value(a, modes[-1])

    def __jtrue(self, a: int, b: int, modes):
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero,
        it sets the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        if self.__value(a, modes[-1]) != 0:
            return self.__value(b, modes[-2])

    def __jfalse(self, a: int, b: int, modes):
        """
        Opcode 6 is jump-if-false: if the first parameter is zero,
        it sets the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        if self.__value(a, modes[-1]) == 0:
            return self.__value(b, modes[-2])

    def __lt(self, a: int, b: int, c:int, modes):
        """
        Opcode 7 is less than: if the first parameter is less than the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        x = self.__value(a, modes[-1])
        y = self.__value(b, modes[-2])
        offset = self.relative_base if modes[-3] == 2 else 0
        self.__memory[c + offset] = 1 if x < y else 0

    def __eq(self, a: int, b: int, c:int, modes):
        """
        Opcode 8 is equals: if the first parameter is equal to the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        x = self.__value(a, modes[-1])
        y = self.__value(b, modes[-2])
        offset = self.relative_base if modes[-3] == 2 else 0
        self.__memory[c + offset] = 1 if x == y else 0

    def __set_base(self, a: int, modes):
        self.relative_base += self.__value(a, modes[-1])
