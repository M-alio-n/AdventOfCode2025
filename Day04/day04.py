def count_neighbors(idx_0: int, idx_1: int, array: list):
    if array[idx_0][idx_1] == '@':
        counter = 0
        for check_0 in [idx_0-1,idx_0,idx_0+1]:
            if check_0<0 or check_0==len(array):
                continue
            for check_1 in [idx_1-1,idx_1,idx_1+1]:
                if check_1<0 or check_1==len(array[0]):
                    continue
                if array[check_0][check_1] == '@':
                    counter += 1
        return counter-1
    return -1

def can_move(idx_0: int, idx_1: int, array: list):
    if -1 < count_neighbors(idx_0, idx_1, array) < 4:
        return True
    return False

### Read input
with open(r'Day04\input04.txt') as f:
    lines = f.readlines()
array = []
for idx, line in enumerate(lines):
    array.append([i for i in line.strip()])

### Part 1
counter_1 = 0
for idx_0, _ in enumerate(array):
    for idx_1, _ in enumerate(array[0]):
        counter_1 += can_move(idx_0, idx_1, array)

print(f'Part 1: {counter_1}')

### Part 2
counter_2 = 0
move_flag = True
while move_flag:
    move_flag = False
    for idx_0, _ in enumerate(array):
        for idx_1, _ in enumerate(array[0]):
            if can_move(idx_0, idx_1, array):
                array[idx_0][idx_1] = '.'
                move_flag = True
                counter_2 += 1
                break
        if move_flag:
            break
                
    
print(f'Part 2: {counter_2}')