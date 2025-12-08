from AoC_util.AoC_loader import AoC_loader
from math import prod

def calc(sign: str, nums: list):
    if sign == '+':
        return sum(nums)
    return prod(nums)
    
### Part 1
lines = AoC_loader(day=6, part='input').get_lines(' ')
new_lines = []
for line in lines[0:-1]:
    new_lines.append([int(i) for i in line if i])
columns = []
for idx in range(len(new_lines[0])):
    columns.append([int(line[idx]) for line in new_lines])

the_sum = 0
for col, sign in zip(columns, [i for i in lines[-1] if i]):
    the_sum += calc(sign, col)

print(f'Part 1: {the_sum}')

### Part 2
lines = AoC_loader(day=6, part='input').get_lines('')

the_sum = 0
nums = []
while lines[0]:
    column = [line.pop() for line in lines]
    if column[-1].strip():
        sign = column.pop()
    if all([i == ' ' for i in column]):
        the_sum += calc(sign, nums)
        nums = []
    else:
        nums.append(int(''.join(column)))

print(f'Part 2: {the_sum+calc(sign,nums)}')