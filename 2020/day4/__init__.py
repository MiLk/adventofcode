def parse_input(lines):
    passports = []
    current = {}
    for line in lines:
        if not line.strip():
            passports.append(current)
            current = {}
            continue
        for field in line.strip().split(' '):
            name, value = field.split(':', maxsplit=1)
            current[name] = value
    passports.append(current)
    return passports


REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def p1(passports):
    return sum(
        set(p.keys()).issuperset(REQUIRED_FIELDS)
        for p in passports
    )


def p2(passports):
    def is_valid(p):
        if not set(p.keys()).issuperset(REQUIRED_FIELDS):
            return False

        if not '1920' <= p['byr'] <= '2002':
            return False

        if not '2010' <= p['iyr'] <= '2020':
            return False

        if not '2020' <= p['eyr'] <= '2030':
            return False

        hv, hu = int(p['hgt'][:-2]), p['hgt'][-2:]
        if hu == 'cm':
            if not 150 <= hv <= 193:
                return False
        elif hu == 'in':
            if not 59 <= hv <= 76:
                return False
        else:
            return False

        hcl = p['hcl']
        if not len(hcl) == 7 or hcl[0] != '#' or any(not ('a' <= c <= 'f' or '0' <= c <= '9') for c in hcl[1:]):
            return False

        if p['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return False

        if len(p['pid']) != 9 or any(not '0' <= c <= '9' for c in p['pid']):
            return False

        return True

    return sum(
        is_valid(p)
        for p in passports
    )
