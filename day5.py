with open('input.txt') as f:
    lines = f.readlines()

fresh_ranges = []
ingredient_ids = []

for line in lines:
    line = line.strip()
    if line == '':
        continue
    pooled = line.split('-')
    if len(pooled) > 1:
        fresh_ranges.append((int(pooled[0]), int(pooled[1])))
    else:
        ingredient_ids.append(int(pooled[0]))


def joinRanges(fresh_range, fresh_range_after):
    if fresh_range[1] >= fresh_range_after[0] and fresh_range[1] <= fresh_range_after[1]:
        return (fresh_range[0],fresh_range_after[1])
    elif fresh_range[1] >= fresh_range_after[0] and fresh_range[1] > fresh_range_after[1]:
        return fresh_range
    return False


def part1(fresh_ranges, ingredient_ids):
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for fresh_range in fresh_ranges:
            if ingredient_id >= fresh_range[0] and ingredient_id <= fresh_range[1]:
                fresh_count += 1
                break
    return fresh_count

def part2(fresh_ranges):
    # yes, i googled the sorting for tuples
    sorted_by_lowest = sorted(fresh_ranges, key=lambda tup: tup[0])
    changed = True
    
    while changed:
        changed = False
        for i in range(len(sorted_by_lowest)):
            if i != len(sorted_by_lowest)-1: #last element should already be OK
                change = joinRanges(sorted_by_lowest[i], sorted_by_lowest[i+1])
                if change:
                    sorted_by_lowest[i] = change
                    sorted_by_lowest.pop(i+1)
                    changed = True
                    break
    
    valid_ids_count = 0
    for ids in sorted_by_lowest:
        valid_ids_count += (ids[1] - ids[0] + 1)
    
    return valid_ids_count

print(str(part1(fresh_ranges, ingredient_ids)))
print(str(part2(fresh_ranges)))