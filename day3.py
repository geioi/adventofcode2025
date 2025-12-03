with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    summa = 0
    for line in lines:
        line = line.rstrip('\r\n')
        highest_first = 0
        highest_second = 0
        highest_changed = False
        for i in range(len(line)):
            if line[i] == '9' and highest_first != 9 and i != len(line)-1:
                highest_first = int(line[i])
                highest_changed = True
            elif i != len(line) - 1 and int(line[i]) > highest_first:
                highest_first = int(line[i])
                highest_changed = True
            elif highest_changed:
                highest_second = int(line[i])
                highest_changed = False
            else:
                if int(line[i]) > highest_second:
                    highest_second = int(line[i])
                
        summa += int(str(highest_first) + str(highest_second))
    return summa

def part2(lines):
    summa = 0
    for line in lines:
        line = line.rstrip('\r\n')
        twelve_best = []
        for i in range(len(line)):
            if len(twelve_best) < 12:
                twelve_best.append(line[i])
            else:
                for j in range(len(twelve_best)):
                    if j == len(twelve_best)-1:
                        if int(twelve_best[j]) < int(line[i]):
                            twelve_best[-1] = line[i]
                    else:
                        if int(twelve_best[j]) < int(twelve_best[j+1]):
                            twelve_best.pop(j)
                            twelve_best.append(line[i])
                            break
        result = ''.join(twelve_best)
        summa += int(result)
    return summa

print(str(part1(lines)))
print(str(part2(lines)))