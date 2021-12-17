#!/usr/bin/env julia

using DelimitedFiles

depths = readdlm("input.txt", '\n', Int)

inc_cnt = 0;
for i in 4:length(depths)
    if depths[i] + depths[i-1] + depths[i-2] > 
       depths[i-1] + depths[i-2] + depths[i-3]
        global inc_cnt += 1
    end
end

print(inc_cnt)