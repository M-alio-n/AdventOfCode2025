from AoC_util.AoC_loader import AoC_loader

###
def max_jolts(bank: str, batteries: int):
    digs = [int(i) for i in bank]
    res_string = ''
    for dig in range(batteries):
        tmp = digs[0:-(batteries-dig-1)]
        if len(tmp) == 0:
            res_string += str(max(rem_digs))
            break
        rem_digs = digs[-(batteries-dig-1):]
        next_dig = max(tmp)
        res_string += str(next_dig)
        digs = tmp[tmp.index(next_dig)+1:] + rem_digs
    return int(res_string)

### Read input
with open(r'Day03\sample03.txt') as f:
    banks = [line.strip() for line in f]

### Part 1
jolts = []
for bank in banks:
    jolts.append(max_jolts(bank, 2))
print(f'Part 1: {sum(jolts)}')

### Part 2
jolts = []
for bank in banks:
    jolts.append(max_jolts(bank ,12))
print(f'Part 2: {sum(jolts)}')