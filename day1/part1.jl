#!/usr/bin/env julia

using DelimitedFiles

depths = readdlm("input.txt", '\n', Int)

inc_cnt = 0;
for i in 2:length(depths)
    if depths[i] > depths[i-1]
        global inc_cnt += 1
    end
end

print(inc_cnt)