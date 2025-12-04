from math import floor
from AoC_util.AoC_loader import AoC_loader

### Functions
class dial:
    def __init__(self, size=100, position=0):
        self.size = size
        self.position_0 = position
        self.position = self.position_0
        self.zero_stops = 0
        self.zero_pass = 0
    
    def get_position(self):
        return self.position
    
    def get_zero_stops(self):
        return self.zero_stops
    
    def get_zero_pass(self):
        return self.zero_pass
    
    def get_all_zeros(self):
        return self.zero_pass+self.zero_stops
    
    def turn_dial(self, direction: str, value: int):
        if direction == 'R':
            if value+self.position>=self.size:
                self.zero_pass += floor((value-(self.size-self.position))/self.size)+1
            self.position = (self.position+value)%self.size
        elif direction == 'L':
            if value>=self.position:
                if self.position == 0:
                    self.zero_pass += floor((value-self.position)/self.size)
                else:
                    self.zero_pass += floor((value-self.position)/self.size)+1
            self.position = (self.position-value)%self.size
        
        if self.position == 0:
            self.zero_stops += 1
            self.zero_pass -= 1
        
my_dial = dial(position=50)


### Part 1 & 2
for line in AoC_loader(day=1, part='input').get_lines():
    my_dial.turn_dial(line[0], int(line[1::]))
print(f'Part 1: {my_dial.get_zero_stops()}')
print(f'Part 2: {my_dial.get_all_zeros()}')