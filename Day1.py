# Advent of Code 2024 Day 1

list1 = []
list2 = []
with open("Inputs/Day1","r") as file:
    for i in file.readlines():
        list1.append(int(i[:6]))
        list2.append(int(i[8:-1]))
list1a = list1.copy()
list2a = list2.copy()

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i]-list2[i])

print(total)

total = 0
for i in list1a:
    a = list2a.count(i)
    total += i*a

print(total)