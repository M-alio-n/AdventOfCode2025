from AoC_util.AoC_loader import AoC_loader
import numpy as np
import matplotlib.pyplot as plt

def compress_reds(reds: dict):
    r_0 = {r[0] for r in reds}
    r_1 = {r[1] for r in reds}
    dim_0_starts, dim_0_lengths = compress_dim(r_0)
    dim_1_starts, dim_1_lengths = compress_dim(r_1)
    # Move corners dim_0
    for red in reds:
        comp_0 = 0
        for idx,start in enumerate(dim_0_starts):
            if start < red[0]:
                comp_0 += dim_0_lengths[idx]
            else:
                break
        comp_1 = 0
        for idx,start in enumerate(dim_1_starts):
            if start < red[1]:
                comp_1 += dim_1_lengths[idx]
            else:
                break
        reds[red] = (red[0]-comp_0, red[1]-comp_1)
    return reds

def compress_dim(dim: set):
    starts = []
    lengths = []
    compression_flag = False
    compression_counter = 0
    compression_start = 0
    for i in range(max(dim)):
        if not compression_flag and i not in dim and i+1 not in dim:
            # Compression starts
            compression_start = i
            compression_counter += 1
            compression_flag = True
        elif compression_flag and i not in dim and i+1 not in dim:
            # Compression continues
            compression_counter += 1
        elif compression_flag and i not in dim and i+1 in dim:
            # Compression ends
            starts.append(compression_start)
            lengths.append(compression_counter)
            compression_flag = False
            compression_counter = 0
    return (starts, lengths)

def green_line(t1: tuple, t2:tuple, green: set):
    if t1[0] == t2[0]:
        start = min(t1[1],t2[1])
        end = max(t1[1],t2[1])
        i = 1
        while start+i < end:
            green.add((t1[0], start+i))
            i += 1
    else:
        start = min(t1[0],t2[0])
        end = max(t1[0],t2[0])
        i = 1
        while start+i < end:
            green.add((start+i, t1[1]))
            i += 1
            
def green_field(green: set, red: set):
    grow = set([(170,170)]) # Manually inspect the data and set the seed in my case (170,170) and for the example (3,6)
    max_0 = max([i[0] for i in red])
    min_0 = min([i[0] for i in red])
    max_1 = max([i[1] for i in red])
    min_1 = min([i[1] for i in red])
    while grow:
        green.update(grow)
        tmp_grow = grow.copy()
        grow = set()
        for g in tmp_grow:
            if not (g[0]+1, g[1]) in green and not (g[0]+1, g[1]) in red and min_0<=g[0]+1<=max_0:
                grow.add((g[0]+1, g[1]))
            if not (g[0]-1, g[1]) in green and not (g[0]-1, g[1]) in red and min_0<=g[0]-1<=max_0:
                grow.add((g[0]-1, g[1]))
            if not (g[0], g[1]+1) in green and not (g[0], g[1]+1) in red and min_1<=g[1]+1<=max_1:
                grow.add((g[0], g[1]+1))
            if not (g[0], g[1]-1) in green and not (g[0], g[1]-1) in red and min_1<=g[1]-1<=max_1:
                grow.add((g[0], g[1]-1))

def legal_field(t1: tuple, t2: tuple, color_fields: set):
    field = set()
    grow = set([t1])
    while grow:
        field.update(grow)
        tmp_grow = grow.copy()
        grow = set()
        for g in tmp_grow:
            if min([t1[0],t2[0]])<=g[0]+1<=max([t1[0],t2[0]]) and not (g[0]+1, g[1]) in field:
                if (g[0]+1, g[1]) in color_fields:
                    grow.add((g[0]+1, g[1]))
                else:
                    return False
            if min([t1[0],t2[0]])<=g[0]-1<=max([t1[0],t2[0]]) and not (g[0]-1, g[1]) in field:
                if (g[0]-1, g[1]) in color_fields:
                    grow.add((g[0]-1, g[1]))
                else:
                    return False
            if min([t1[1],t2[1]])<=g[1]+1<=max([t1[1],t2[1]]) and not (g[0], g[1]+1) in field:
                if (g[0], g[1]+1) in color_fields:
                    grow.add((g[0], g[1]+1))
                else:
                    return False
            if min([t1[1],t2[1]])<=g[1]-1<=max([t1[1],t2[1]]) and not (g[0], g[1]-1) in field:
                if (g[0], g[1]-1) in color_fields:
                    grow.add((g[0], g[1]-1))
                else:
                    return False
    return True

### Load the input
red = [tuple(r) for r in AoC_loader(day=9, part='input').get_lines(',',as_type=int)]

### Part 1
rectangles = []
for t1_idx, t1 in enumerate(red):
    for t2 in red[t1_idx+1:]:
        rectangles.append((abs((abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)),t1,t2))
rectangles.sort(key=lambda rect: rect[0], reverse=True)
print(f'Part 1: {rectangles[0][0]}')

### Part 2
red_conv = {r: None for r in red}
# Compress to 1 between reds
red_conv = compress_reds(red_conv)
green = set()
for t1_idx in range(1,len(red)):
    green_line(red_conv[red[t1_idx]], red_conv[red[t1_idx-1]], green)
green_line(red_conv[red[0]], red_conv[red[-1]], green)
## Manual inspection of the data
# max_0 = max(i[0] for i in red_conv.values())
# max_1 = max(i[1] for i in red_conv.values())
# array = np.zeros((max_0+1, max_1+1))
# for r in red_conv.values():
#     array[r] = 2
# for r in green:
#     array[r] = 1
# plt.imshow(array)
# plt.show()
# There are no pockets/islands in the AoC data!
green_field(green, set(i for i in red_conv.values())) # Manually set the seed for the green field
color_fields = green.union(set(i for i in red_conv.values()))

for idx,rect in enumerate(rectangles):
    if idx % 1000 == 0:
        print(f'Checking rectangle {idx} of {len(rectangles)}')
    if legal_field(red_conv[rect[1]], red_conv[rect[2]], color_fields):
        print(f'Part 2: {rect[0]}')
        break
        