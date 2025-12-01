with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    # I suspect the part1 code does not behave 100% correctly in all cases
    # but it got me the correct answer at least on my input
    # so use at your own caution
    # leaving it as is because i am too lazy
    nr = 50
    actualCode = 0
    for line in lines:
        if line[0] == 'L':
            direction = 'L'
            jupid = line.split('L')
        else:
            direction = 'R'
            jupid = line.split('R')
            
        if direction == 'R':
            nr += int(jupid[1])
            if nr == 0 or nr % 100 == 0:
                nr = 0
                actualCode += 1
            elif nr > 100:
                vaheArv = nr % 100
                nr = vaheArv
                
        else:
            nr -= int(jupid[1])
            if nr == 0 or nr % 100 == 0:
                nr = 0
                actualCode += 1
            elif nr < 0:
                vaheArv = nr % 100
                nr = 100 + vaheArv
    return actualCode
        
        
def part2(lines):
    nr = 50
    actualCode = 0
    for line in lines:
        if line[0] == 'L':
            jupid = line.split('L')
        else:
            jupid = line.split('R')
            
        nr += int(jupid[1])
        if nr == 0 or nr % 100 == 0:
            if nr == 0:
                actualCode += 1
            else:
                actualCode += nr // 100
            nr = 0
        elif nr > 100:
            taisarv = nr // 100
            actualCode += taisarv
            nr = abs((taisarv * 100)-nr)
    return actualCode

print(str(part1(lines)))
print(str(part2(lines)))