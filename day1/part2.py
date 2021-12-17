#!/usr/bin/env python3

with open('input.txt') as f:
    depths = f.read().splitlines()

depth_list = []
for depth in depths:
    depth_list.append(int(depth))

inc_count = 0
for i, depth in enumerate(depth_list):
    if depth_list[i] + depth_list[i-1] + depth_list[i-2] > \
       depth_list[i-1] + depth_list[i-2] + depth_list[i-3]:
        inc_count += 1

print(inc_count)    
