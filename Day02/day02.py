from AoC_util.AoC_loader import AoC_loader

### Functions
def check_range_1(val1: int, val2: int):
    invalid = []
    for num in range(val1, val2+1):
        if len(str(num))%2 == 0:
            if str(num)[0:int(len(str(num))/2)] == str(num)[int(len(str(num))/2):]:
                invalid.append(num)
    return invalid

def check_range_2(val1: int, val2: int):
    invalid = set()
    for num in range(val1, val2+1):
        lens = [i for i in range(1,int(len(str(num))/2)+1) if len(str(num))%i==0]
        for cur_len in lens:
            parts = [str(num)[cur_len*i:cur_len*(i+1)] for i in range(0,int(len(str(num))/cur_len))]
            if len(set(parts)) == 1:
                invalid.add(num)
    return invalid
    
### Read input
ranges = AoC_loader(day=2, part='input').get_lines(',')

### Part 1
invalid_1 = []
for curr_range in ranges:
    invalid_1 = invalid_1 + check_range_1(int(curr_range.split('-')[0]), int(curr_range.split('-')[1]))

print(f'Part 1: {sum(invalid_1)}')

### Part 2
invalid_2 = set()
for curr_range in ranges:
    invalid_2 = invalid_2.union(check_range_2(int(curr_range.split('-')[0]), int(curr_range.split('-')[1])))

print(f'Part 2: {sum(invalid_2)}')