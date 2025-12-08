from AoC_util.AoC_loader import AoC_loader
from math import prod
import numpy as np

def connect_next(distances: np.array, circuits: list, boxes: list, connected: set):
    idx = tuple(np.argwhere(distances==distances.min())[0])
    a = boxes[idx[0]]
    b = boxes[idx[1]]
    distances[idx[0], idx[1]] = np.inf
    if a in connected and b in connected:
        a_idx = False
        b_idx = False
        for circ_idx, circ in enumerate(circuits):
            if a in circ:
                a_idx = circ_idx
                if b_idx:
                    break
            if b in circ:
                b_idx = circ_idx
                if a_idx:
                    break
        if a_idx != b_idx:
            pop_circ = circuits.pop(max([a_idx, b_idx]))
            circuits[min([a_idx, b_idx])] = circuits[min([a_idx, b_idx])].union(pop_circ)
        return (a,b)
    if a in connected or b in connected:
        for circ in circuits:
            if a in circ:
                circ.add(b)
                break
            if b in circ:
                circ.add(a)
                break
    else:
        circuits.append(set((a,b)))
    connected.add(a)
    connected.add(b)
    return (a, b)
    
### Load the input
boxes = [tuple(i) for i in AoC_loader(day=8, part='input').get_lines(',',as_type=int)]

distances = np.zeros((len(boxes), len(boxes)))
for idx_0,a in enumerate(boxes):
    for idx_1 in range(idx_0+1, len(boxes)):
        distances[idx_0, idx_1] = np.sqrt(sum([(a[i]-boxes[idx_1][i])**2 for i in range(3)]))
distances[distances==0] = np.inf

### Part 1
connected = set()
circuits = []
for i in range(1000):
    _ = connect_next(distances, circuits, boxes, connected)
print(f'Part 1:{prod(sorted([len(i) for i in circuits])[-3:])}')
### Part 2
while len(circuits) != 1 or len(circuits[0]) != len(boxes):
    final_pair = connect_next(distances, circuits, boxes, connected)
print(f'Part 2: {final_pair[0][0] * final_pair[1][0]}')