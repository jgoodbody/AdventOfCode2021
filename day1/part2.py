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

# actual function for this
def depth_increaser(depths, sample_size):
    inc_count = 0
    for i in range(len(depths)-sample_size):
        if sum(depths[i:i+sample_size]) > sum(depths[i-1:i-1+sample_size]):
            inc_count +=1
    return inc_count

print(depth_increaser(depth_list, 3))