from AoC_util.AoC_loader import AoC_loader
import numpy as np
from time import time

permutations = dict()

def start_machine(machine: list):
    target = [i=='#' for i in machine[0][1:-1]]
    buttons = [butt[1:-1].split(',') for butt in machine[1:-1]]
    for i, entry in enumerate(buttons):
        buttons[i] = list(map(int, entry))
    perms = permute(len(machine)-2)
    for perm in perms:
        sequence = [False for i in range(len(target))]
        for idx, state in enumerate(perm):
            if state:
                for light in buttons[idx]:
                    sequence[light] = not sequence[light]
                    pass
        if sequence == target:
            return sum(perm)
    return 0 # This should never happen

def permute(buttons: int):
    if not buttons in permutations:    
        perms = [[False],[True]]
        while len(perms[False]) < buttons:
            tmp_perms = []
            for i in range(len(perms)):
                curr = perms.pop()
                tmp_perms.append(curr+[False])
                tmp_perms.append(curr+[True])
            perms = tmp_perms
        permutations.update({buttons: sorted(perms, key=sum)[1::]})
    return permutations[buttons]

### Get input
machines = AoC_loader(day=10, part='input').get_lines(seperator=' ')

### Part 1
button_presses = 0
for machine in machines:
    button_presses += start_machine(machine)
print(f'Part 1: {button_presses}')