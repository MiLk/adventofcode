from dataclasses import dataclass
from typing import List, Callable, Dict, Tuple


@dataclass
class Instruction:
    parameters: int
    fn: Callable[..., None]


class Computer:
    def __init__(self, memory: List):
        self.__memory = list(memory)

        self.__opcodes: Dict[int, Instruction] = {
            1: Instruction(3, self.__add),
            2: Instruction(3, self.__mul),
        }

    def run(self, initialization: List[Tuple]):
        for address, value in initialization:
            self.__memory[address] = value

        ip = 0
        while (opcode := self.__memory[ip]) != 99:
            instruction = self.__opcodes[opcode]
            instruction.fn(*self.__parameters(ip, instruction))
            ip += 1 + instruction.parameters
        return self.__memory[0]

    def __parameters(self, ip, instruction):
        return self.__memory[ip + 1:ip + 1 + instruction.parameters]

    def __add(self, a, b, c):
        self.__memory[c] = self.__memory[a] + self.__memory[b]

    def __mul(self, a, b, c):
        self.__memory[c] = self.__memory[a] * self.__memory[b]
