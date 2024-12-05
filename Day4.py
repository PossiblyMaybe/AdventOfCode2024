import re

def check_direction(index, pos, grid):
    pos2 = [index[0] + pos[0], index[1] + pos[1]]
    if 0 <= pos2[0] < len(grid) and 0 <= pos2[1] < len(grid[0]):
        pos3 = [index[0] + pos2[0], index[1] + pos2[1]]
        if grid[pos2[0]][pos2[1]] == 'A':
            if 0 <= pos3[0] < len(grid) and 0 <= pos3[1] < len(grid[0]):
                if grid[pos3[0]][pos3[1]] == 'S':
                    return 1
    return 0


def check3x3(index, grid):
    found = 0
    for i in range(9):
        pos = [index[0] + (i // 3) - 1, index[1] + (i % 3) - 1]
        if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
            if grid[pos[0]][pos[1]] == "M":
                found += check_direction([(i // 3) - 1, (i % 3) - 1], pos, grid)

    return found


def part_1(file):
    line_list = []
    with open(file) as f:
        for i in f:
            line_list.append(i.strip("\n"))
    for i in line_list:
        i.strip()
    count = 0
    for i in range(len(line_list)):
        for j in range(len(line_list[i])):
            if line_list[i][j] == 'X':
                count += check3x3([i, j], line_list)

    print(count)

def check3x3_2(index, grid):
    section = ""
    for i in range(9):
        pos = [index[0] + (i // 3) - 1, index[1] + (i % 3) - 1]
        if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
            return 0
        section += grid[pos[0]][pos[1]]
    if re.match("(M.S.A.M.S)|(M.M.A.S.S)|(S.S.A.M.M)|(S.M.A.S.M)",section) is not None:
        return 1
    return 0


def part_2(file):
    line_list = []
    with open(file) as f:
        for i in f:
            line_list.append(i.strip("\n"))#
    for i in line_list:
        i.strip()
    count = 0
    for i in range(len(line_list)):
        for j in range(len(line_list[i])):
            if line_list[i][j] == 'A':
                count += check3x3_2([i, j], line_list)
    print(count)


part_1("Inputs/Day4")
part_2("Inputs/Day4")