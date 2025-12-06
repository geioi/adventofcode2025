with open('input.txt') as f:
    lines = f.readlines()
    
def part1(lines):
    numbers_arr = []
    symbols = []
    for line in lines:
        line = line.lstrip().rstrip()
        pieces = line.split()
        numbers = []
        isDigitRow = True
        for piece in pieces:
            if piece.isdigit():
                numbers.append(int(piece))
            else:
                symbols.append(piece)
                isDigitRow = False
        if isDigitRow:
            numbers_arr.append(numbers)
    summa = 0
    for i in range(len(numbers_arr[0])): # we can assume all the rows are the same length anyway
        result = 0
        for j in range(len(numbers_arr)):
            if symbols[i] == '*':
                if result == 0:
                    result = numbers_arr[j][i]
                else:  
                    result *= numbers_arr[j][i]
            if symbols[i] == '+':
                result += numbers_arr[j][i]
        summa += result
    
    return summa

def part2(lines):
    locs = {}
    for line in lines:
        line = line.strip('\n')
        for i in range(len(line)):
            if line[i] != ' ':
                if i in locs:
                    locs[i].append(line[i])
                else:
                    locs[i] = [line[i]]
    
    locs = dict(sorted(locs.items()))
    
    current_op = ''
    summa = 0
    result = 0
    for values in locs.values():
        if '*' in values or '+' in values:
            current_op = values[-1] # it is always the last element in there
            summa += result
            result = 0
            values.pop()
            result = int(''.join(values))
        elif current_op == '+':
            result += int(''.join(values))
        else:
            result *= int(''.join(values))

    summa += result #ensure that the last result gets added as well to total sum
    return summa
        

print(str(part1(lines)))
print(str(part2(lines)))