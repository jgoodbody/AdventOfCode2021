#!/usr/bin/env julia

using DelimitedFiles

diag_report = readdlm("input.txt", '\n', String)

function gamma_rate(report)
    digit_counts = zeros(length(report[1]))
    for num in report
        for (place, digit) in enumerate(num)
            if digit == '1'
                digit_counts[place] += 1
            else
                digit_counts[place] -= 1
            end
        end
    end
    binary_counter = String[]
    for i in digit_counts
        if i >= 0
            push!(binary_counter, "1")
        else
            push!(binary_counter, "0")
        end
    end
    return join(binary_counter[:])
end

function epsilon_rate(gamma)
    epsilon = String[]
    for digit in gamma
        if digit == '1'
            push!(epsilon, "0")
        else
            push!(epsilon, "1")
        end
    end
    return join(epsilon[:])
end

print(parse(Int, gamma_rate(diag_report); base=2) * parse(Int, epsilon_rate(gamma_rate(diag_report)); base=2))