def read_input(folder: str, strip: bool = True) -> list[str]:
    with open(f"{folder}/input.txt") as f:
        lines = f.readlines()
    if not strip:
        return lines
    return [stripped for line in lines if (stripped := line.strip())]


def int_line(line: str) -> int:
    return int(line.strip())


def int_list_line(line: str, sep="\t") -> list[int]:
    return [int(n) for n in line.strip().split(sep)]


def str_list_line(line, sep="\t") -> list[str]:
    return [n for n in line.strip().split(sep)]
