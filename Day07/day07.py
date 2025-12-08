from AoC_util.AoC_loader import AoC_loader
import numpy as np

def propagate(beams: dict, array: np.array):
    split_counter = 0
    timeline_counter = 0
    while beams:
        new_beams = {}
        for beam in beams:
            if beam[0]+1 < array.shape[0] and array[beam[0]+1,beam[1]] == '^':
                if not (beam[0]+1, beam[1]+1) in new_beams:
                    new_beams.update({(beam[0]+1, beam[1]+1): beams[beam]})
                else:
                    new_beams[(beam[0]+1, beam[1]+1)] += beams[beam]
                if not (beam[0]+1, beam[1]-1) in new_beams:
                    new_beams.update({(beam[0]+1, beam[1]-1): beams[beam]})
                else:
                    new_beams[(beam[0]+1, beam[1]-1)] += beams[beam]
                split_counter += 1
            elif beam[0]+1 < array.shape[0] and array[beam[0]+1,beam[1]] == '.':
                if (beam[0]+1,beam[1]) in new_beams:
                    new_beams[(beam[0]+1,beam[1])] += beams[beam]
                else:
                    new_beams.update({(beam[0]+1,beam[1]): beams[beam]})
            else:
                timeline_counter += beams[beam]
        beams = new_beams
    return (split_counter, timeline_counter)

### Load input
array = AoC_loader(day=7, part='input').get_array('')

### Part 1 & 2
beams = {(int(np.where(array == 'S')[0][0]), int(np.where(array == 'S')[1][0])): 1}
result = propagate(beams, array)
print(f'Part 1: {result[0]}')
print(f'Part 2: {result[1]}')
