from utils.file import read_input


def _find_best_2(bank: str) -> int:
    m = max(int(b) for b in bank[:-1])
    idx = bank.index(str(m))
    m2 = max(int(b) for b in bank[idx + 1 :])
    return m * 10 + m2


def _find_best_n(bank: str, n: int = 12) -> int:
    if n == 1:
        return max(int(b) for b in bank)
    m = max(int(b) for b in bank[: -(n - 1)])
    idx = bank.index(str(m))
    m_next = _find_best_n(bank[idx + 1 :], n - 1)
    return m * 10 ** (n - 1) + m_next


def main() -> None:
    banks = read_input(__package__)
    total, total_2 = 0, 0
    for bank in banks:
        total += _find_best_n(bank, 2)
        total_2 += _find_best_n(bank, 12)
    print(total)
    print(total_2)


if __name__ == "__main__":
    main()
