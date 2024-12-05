# My code here is utter dogshit, but it works so yk

def get_rules_orders(file):
    with open(file) as f:
        a = list(map(str.strip, f.readlines()))
    index = a.index("")
    rules = {}
    for i in [j.split("|") for j in a[:index]]:
        if i[1] in rules.keys():
            rules[i[1]].append(i[0])
        else:
            rules[i[1]] = [i[0]]

    print_orders = list(map(lambda x: x.split(","), a[index + 1:]))
    return rules, print_orders


def get_rules2(file):
    with open(file) as f:
        a = list(map(str.strip, f.readlines()))
    index = a.index("")
    rules = {}
    for i in [j.split("|") for j in a[:index]]:
        if i[0] in rules.keys():
            rules[i[0]].append(i[1])
        else:
            rules[i[0]] = [i[1]]

    print_orders = list(map(lambda x: x.split(","), a[index + 1:]))
    return rules


def sum_mid(orders):
    total = 0
    for i in orders:
        total += int(i[(len(i) // 2)])
    return total


def part_1(file):
    rules, print_orders = get_rules_orders(file)
    good_orders = []
    for order in print_orders:
        disallowed = []
        good = True
        for num in order:
            if num in disallowed:
                good = False
                break
            else:
                if num in rules.keys():
                    disallowed += rules[num]
        if good:
            good_orders.append(order)
    return sum_mid(good_orders)


def part_2(file):
    rules, print_orders = get_rules_orders(file)
    rules2 = get_rules2(file)
    bad_orders2 = print_orders

    while len(bad_orders2) > 0:
        good_orders = []
        bad_orders = []
        wrong_items = []
        for order in bad_orders2:
            disallowed = []
            wrong = []
            good = True
            for index, num in enumerate(order):
                if num in disallowed:
                    good = False
                    wrong.append(index)
                else:
                    if num in rules.keys():
                        disallowed += rules[num]
            if not good:
                wrong_items.append(wrong)
                bad_orders.append(order)

        for order in print_orders:
            disallowed = []
            good = True
            for num in order:
                if num in disallowed:
                    good = False
                    break
                else:
                    if num in rules.keys():
                        disallowed += rules[num]
            if good:
                good_orders.append(order)

        for j in range(len(bad_orders)):
            for i in wrong_items[j]:
                sort = False
                index = i
                while not sort:
                    index -= 1
                    temp = bad_orders[j][i]
                    bad_orders[j][i] = bad_orders[j][i - 1]
                    bad_orders[j][i - 1] = temp
                    if bad_orders[j][i] in rules2[bad_orders[j][i - 1]]:
                        sort = True

        bad_orders2 = bad_orders
    return sum_mid(good_orders)-part_1(file)


print(part_1("Inputs/Day5"))
print(part_2("Inputs/Day5"))
