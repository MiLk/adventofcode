from dataclasses import dataclass
from typing import List, Callable, Dict, Tuple, Optional


@dataclass
class Instruction:
    parameters: int
    fn: Callable[..., Optional[int]]


class Computer:
    def __init__(self, memory: List[int]):
        self.__memory = list(memory)

        self.__opcodes: Dict[int, Instruction] = {
            1: Instruction(3, self.__add),
            2: Instruction(3, self.__mul),
            3: Instruction(1, self.__save),
            4: Instruction(1, self.__load),
            5: Instruction(2, self.__jtrue),
            6: Instruction(2, self.__jfalse),
            7: Instruction(3, self.__lt),
            8: Instruction(3, self.__eq),
        }

        self.input = None
        self.output = None

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
            modes = tuple(int(m) for m in opcode_mode[:-2].zfill(2))
            if not modes:
                modes = (0, 0)
            instruction = self.__opcodes[opcode]
            jump = instruction.fn(*self.__parameters(ip, instruction), modes)
            if jump:
                ip = jump
            else:
                ip += 1 + instruction.parameters
        return self.__memory[0]

    def __parameters(self, ip: int, instruction: Instruction):
        return self.__memory[ip + 1:ip + 1 + instruction.parameters]

    def __add(self, a: int, b: int, c: int, modes=(0, 0)):
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        self.__memory[c] = x + y

    def __mul(self, a: int, b: int, c: int, modes=(0, 0)):
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        self.__memory[c] = x * y

    def __save(self, a: int, _modes):
        """
        Opcode 3 takes a single integer as input and saves it to the address given by its only parameter.
        For example, the instruction 3,50 would take an input value and store it at address 50.
        """
        self.__memory[a] = self.input

    def __load(self, a: int, modes):
        """
        Opcode 4 outputs the value of its only parameter.
        For example, the instruction 4,50 would output the value at address 50.
        """
        x = a if modes[-1] == 1 else self.__memory[a]
        self.output = x

    def __jtrue(self, a: int, b: int, modes):
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero,
        it sets the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        if x != 0:
            return y

    def __jfalse(self, a: int, b: int, modes):
        """
        Opcode 6 is jump-if-false: if the first parameter is zero,
        it sets the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        if x == 0:
            return y

    def __lt(self, a: int, b: int, c:int, modes):
        """
        Opcode 7 is less than: if the first parameter is less than the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        self.__memory[c] = 1 if x < y else 0

    def __eq(self, a: int, b: int, c:int, modes):
        """
        Opcode 8 is equals: if the first parameter is equal to the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        x = a if modes[-1] == 1 else self.__memory[a]
        y = b if modes[-2] == 1 else self.__memory[b]
        self.__memory[c] = 1 if x == y else 0
