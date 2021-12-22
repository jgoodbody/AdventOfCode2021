#!/usr/bin/env julia

using DelimitedFiles

moves = readdlm("input.txt", '\n')

function f(moves)
    horizontal = 0; depth = 0
    for move in moves
        direction, magnitude = split(move,' ')
        if direction == "forward"
            horizontal += parse(Int64, magnitude)
        elseif direction == "down"
            depth += parse(Int64, magnitude)
        else
            depth -= parse(Int64, magnitude)
        end
    end
    return horizontal*depth
end

print(f(moves))