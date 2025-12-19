from utils.file import read_input


def main() -> None:
    lines = read_input(__package__)
    rotations = [(-1 if line[0] == "L" else 1, int(line[1:])) for line in lines]
    password, password_2 = 0, 0
    dial = 50
    for direction, distance in rotations:
        if direction > 0:
            password_2 += int((dial + distance) / 100)
        else:
            mirrored = (100 - dial) % 100
            password_2 += int((mirrored + distance) / 100)
        dial += direction * distance
        dial %= 100
        if dial == 0:
            password += 1
    print(password)
    print(password_2)


if __name__ == "__main__":
    main()
