import re


def mul(a,b):
    return a*b

def part_1():
    total = 0
    with open("Inputs/Day3") as file:
        for line in file:
            a = re.findall("mul\\([0-9]+,[0-9]+\\)",line)
            for i in a:
                total += eval(i)

    print(total)

def part_2():
    full_str = ""
    total = 0
    with open("Inputs/Day3") as file:
        for line in file:
            full_str += line.strip()
    full_str = re.sub(r"don't\(\).*?do\(\)","",full_str)

    a = re.findall("mul\\([0-9]+,[0-9]+\\)", full_str)
    for i in a:
        total += eval(i)
    print(total)

part_1()
part_2()