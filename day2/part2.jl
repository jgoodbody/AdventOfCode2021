#!/usr/bin/env julia

using DelimitedFiles

moves = readdlm("input.txt", '\n')

function f(moves)
    horizontal = 0; depth = 0; aim = 0
    for move in moves
        direction, magnitude = split(move,' ')
        if direction == "forward"
            horizontal += parse(Int64, magnitude)
            depth += parse(Int64, magnitude)*aim
        elseif direction == "down"
            aim += parse(Int64, magnitude)
        else
            aim -= parse(Int64, magnitude)
        end
    end
    return horizontal*depth
end

print(f(moves))