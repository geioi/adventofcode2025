with open('input.txt') as f:
    lines = f.readlines()

def createPadding(lines):
    playfield = []
    paddedRow = []
    exampleRow = lines[0].strip()
    for char in exampleRow:
        paddedRow.append('&')
    
    # add 2 more to create a complete box
    paddedRow.append('&')
    paddedRow.append('&')
    
    playfield.append(paddedRow)
    
    for line in lines:
        line = list(line.strip())
        line.insert(0, '&')
        line.append('&')
        playfield.append(line)
    playfield.append(paddedRow)
    
    return playfield

def findAdjacentRollsCount(upper, middle, lower, pos):
    roll_count = 0
    if upper[pos-1] == '@' or upper[pos-1] == 'x':
        roll_count += 1
    if upper[pos] == '@' or upper[pos] == 'x':
        roll_count += 1
    if upper[pos+1] == '@' or upper[pos+1] == 'x':
        roll_count += 1
    if middle[pos-1] == '@' or middle[pos-1] == 'x':
        roll_count += 1
    if middle[pos+1] == '@' or middle[pos+1] == 'x':
        roll_count += 1
    if lower[pos-1] == '@' or lower[pos-1] == 'x':
        roll_count += 1
    if lower[pos] == '@' or lower[pos] == 'x':
        roll_count += 1
    if lower[pos+1] == '@' or lower[pos+1] == 'x':
        roll_count += 1
        
    return roll_count

def resetPlayField(playfield):
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if playfield[i][j] == 'x':
                playfield[i][j] = '.'
    return playfield
    

def part1(lines):
    playfield = createPadding(lines)
    result = 0
    for i in range(len(playfield)):
        for j in range(len(playfield[i])):
            if playfield[i][j] == '&':
                continue
            if playfield[i][j] == '@':
                roll_count = findAdjacentRollsCount(playfield[i-1], playfield[i], playfield[i+1], j)
                if roll_count < 4:
                    result += 1
                    playfield[i][j] = 'x'
    return result

def part2(lines):
    playfield = createPadding(lines)
    result = 0
    intermediate_result = -1 # set it to whatever nr that != 0 just so the first while check passes
    while intermediate_result != 0:
        intermediate_result = 0
        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                if playfield[i][j] == '&':
                    continue
                if playfield[i][j] == '@':
                    roll_count = findAdjacentRollsCount(playfield[i-1], playfield[i], playfield[i+1], j)
                    if roll_count < 4:
                        intermediate_result += 1
                        playfield[i][j] = 'x'
        result += intermediate_result
        playfield = resetPlayField(playfield)
    return result

print(str(part1(lines)))
print(str(part2(lines)))