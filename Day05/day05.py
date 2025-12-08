from AoC_util.AoC_loader import AoC_loader

def combine_ranges(ranges: list):
    combined_ranges=[]
    while fresh:
        curr_range = fresh.pop(0)
        while len(fresh) > 0 and fresh[0][0] <= curr_range[1]:
            tmp = fresh.pop(0)
            curr_range[1] = max(curr_range[1],tmp[1])
        combined_ranges.append(curr_range)
    return combined_ranges

def analyze_fresh(fresh: list):
    counter = 0
    for fresh_range in fresh:
        counter += fresh_range[1] - fresh_range[0] + 1
    return counter

def analyze_available(fresh: list, available: list):
    range_idx = 0
    fresh_count = 0
    for check in available:
        while range_idx < len(fresh):
            if check < fresh[range_idx][0]:
                break
            if fresh[range_idx][0] <= check <= fresh[range_idx][1]:
                fresh_count += 1
                break
            if check > fresh[range_idx][1]:
                range_idx += 1
    return fresh_count

### Get sorted input
loader = AoC_loader(day=5, part='input')
fresh = sorted(loader.get_lines('-',0,int))
fresh = combine_ranges(fresh)
available = sorted(loader.get_lines(part_index=1,as_type=int))

### Part 1
print(f'Part 1: {analyze_available(fresh, available)}')
### Part 2
print(f'Part 2: {analyze_fresh(fresh)}')