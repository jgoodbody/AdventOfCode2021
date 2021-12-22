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

# actual function!
function f(depths, sample_size)
    inc_count = 0;
    for i in 1:(length(depths)-sample_size)
        if sum(depths[i+1:i+sample_size]) > sum(depths[i:i+sample_size-1])
            inc_count += 1
        end
    end
    return inc_count
end

print(f(depths, 3))