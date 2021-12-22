#!/usr/bin/env python3

with open('input.txt') as f:
    moves = f.read().splitlines()

move_list = []
for move in moves:
    move_list.append(move)

def sub_position(moves):
    horizontal = 0; depth = 0
    for move in moves:
        direction, magnitude = move.split(' ')
        if direction == 'forward':
            horizontal += int(magnitude)
        elif direction == 'down':
            depth += int(magnitude)
        else:
            depth -= int(magnitude)
    return horizontal*depth

print(sub_position(move_list))
