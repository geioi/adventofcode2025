with open('input.txt') as f:
    lines = f.readlines()

def part1(lines):
    for line in lines:
        id_ranges = line.split(',')
    summa = 0
    for id_range in id_ranges:
        pooled = id_range.split('-')
        lowest = int(pooled[0])
        highest = int(pooled[1])
        
        for i in range(lowest, highest+1, 1):
            as_str = str(i)
            if len(as_str) % 2 == 0:
                if as_str[:len(as_str)//2] == as_str[len(as_str)//2:]:
                    summa += i
        
    return summa

def part2(lines):
    for line in lines:
        id_ranges = line.split(',')
    summa = 0
    for id_range in id_ranges:
        pooled = id_range.split('-')
        lowest = int(pooled[0])
        highest = int(pooled[1])
        
        for i in range(lowest, highest+1, 1):
            as_str = str(i)
            if len(as_str) % 2 == 0:
                if as_str[:len(as_str)//2] == as_str[len(as_str)//2:]:
                    summa += i
                else:
                    if len(as_str) != 2:
                        is_same_numbers = True
                        current_nr = as_str[:2]
                        for j in range(2, len(as_str), 2):
                            if current_nr != as_str[j:j+2]:
                                is_same_numbers = False
                        if is_same_numbers:
                            summa += i
            else:
                if len(as_str) % 3 == 0 and len(as_str) != 3:
                    if as_str[:3] == as_str[3:6] and as_str[:3] == as_str[-3:]:
                        summa += i
                else:
                    if len(as_str) != 1:
                        is_same_numbers = True
                        current_nr = as_str[0]
                        for j in as_str:
                            if j != current_nr:
                                is_same_numbers = False
                        if is_same_numbers:
                            summa += i  
        
    return summa


print(str(part1(lines)))
print(str(part2(lines)))