from sys import prefix


def is_safe(levels: list):
    new = []
    bad_level_count = 0
    for i in range(1, len(levels)):
        new.append(levels[i] - levels[i - 1])
    if max(new) > 0 > min(new):
        return False
    new = list(map(abs, new))
    if max(new) > 3:
        return False
    if min(new) < 1:
        return False
    return True


def is_safe2(levels: list):
    if is_safe(levels):
        return True
    safe = False
    for i in range(len(levels) - 1):
        if is_safe(levels[:i] + levels[i + 1:]):
            safe = True
    if is_safe(levels[:-1]):
        safe = True
    return safe


safe_count = 0
with open("Inputs/Day2") as file:
    for line in file.readlines():
        a = list(map(int, line.strip().split(" ")))
        if is_safe2(a):
            safe_count += 1
print(safe_count)
