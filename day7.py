with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    splitters = {}
    starting_position = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                starting_position = j
            elif lines[i][j] == '^':
                if i in splitters:
                    splitters[i].append(j)
                else:
                    splitters[i] = [j]
    splitters = dict(sorted(splitters.items()))
    
    splits = 0
    tachyon_beams = {starting_position}
    for i in range(len(lines)):
        if i in splitters:
            for splitter in splitters[i]:
                if splitter in tachyon_beams:
                    tachyon_beams.remove(splitter)
                    tachyon_beams.add(splitter-1)
                    tachyon_beams.add(splitter+1)
                    splits += 1
                    
        
    return splits

def part2 (lines):
    splitters = {}
    starting_position = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                starting_position = j
            elif lines[i][j] == '^':
                if i in splitters:
                    splitters[i].append(j)
                else:
                    splitters[i] = [j]
    splitters = dict(sorted(splitters.items()))
    
    traverse_counts = {starting_position: 1}
    for i in range(len(lines)):
        for k, v in list(traverse_counts.items()):
            if i in splitters:
                if k in splitters[i]:
                    traverse_counts[k-1] = traverse_counts.get(k-1, 0) + v
                    traverse_counts[k+1] = traverse_counts.get(k+1, 0) + v
                    traverse_counts.pop(k)
    return sum(traverse_counts.values())

print(str(part1(lines)))
print(str(part2(lines)))