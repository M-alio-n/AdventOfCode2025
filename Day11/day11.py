from AoC_util.AoC_loader import AoC_loader

def reverse_search(start: str, targets: set(), devices: dict, iteration: int=0, main_target: str=None, update_needed: dict={}):
    if iteration == 0:
        main_target = list(targets)[0]
        next_steps = get_steps(targets, devices)
        for i in next_steps:
            devices[i][main_target] = 1
    else:
        next_steps = get_steps(targets, devices)
        for i in next_steps:
            devices[i][main_target] = sum(devices[a][main_target] for a in devices[i]['connects'] if main_target in devices[a])
    if next_steps:
        reverse_search(start, next_steps, devices, iteration+1, main_target, update_needed)
    return

def get_steps(targets: set, devices: dict):
    next_steps = set()
    for target in targets:
        for key, val in devices.items():
            if target in val['connects']:
                next_steps.add(key)
    return next_steps

### Load input
devices = AoC_loader(day=11, part='input').get_lines(' ')
devices = {a[0][0:-1]: {'connects': set(a[1::])} for a in devices}

### Part 1
# simplify(devices)
reverse_search('you',set(['out']),devices)
print(f'Part 1: {devices["you"]["out"]}')

### Part 2
reverse_search('svr',set(['fft']),devices)
print(f'svr-fft: {devices["svr"]["fft"]}')
reverse_search('fft',set(['dac']),devices)
print(f'fft-dac: {devices["fft"]["dac"]}')
reverse_search('dac',set(['out']),devices)
print(f'dac-out: {devices["dac"]["out"]}')

print(f'Part 2: {devices["svr"]["fft"]*devices["fft"]["dac"]*devices["dac"]["out"]}')