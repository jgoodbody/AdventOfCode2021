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

function epsilon_rate(report)
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
            push!(binary_counter, "0")
        else
            push!(binary_counter, "1")
        end
    end
    return join(binary_counter[:])
end

# i have no idea how to correctly make a null value in julia. why does nothing not work.
# should i be using missing? wtf.
function oxygen_gen_rating(report, most_common)
    len = length(report)
    filtered = report[:]
    for i in 1:len
        for (index, num) in enumerate(filtered)
            if num[i] != most_common[i]
                filtered[index] = repeat("z", length(num))
            end
        end
        filtered = filter(x -> x != repeat("z", length(filtered[1])), filtered)
        len = length(filtered)
        most_common = gamma_rate(filtered)
        if len == 1
            return filtered[1]
        end
    end
    return most_common
end

function CO2_scrub_rating(report, least_common)
    len = length(report)
    filtered = report[:]
    for i in 1:len
        for (index, num) in enumerate(filtered)
            if num[i] != least_common[i]
                filtered[index] = repeat("z", length(num))
            end
        end
        filtered = filter(x -> x != repeat("z", length(filtered[1])), filtered)
        len = length(filtered)
        least_common = epsilon_rate(filtered)
        if len == 1
            return filtered[1]
        end
    end
    return least_common
end

gamma = gamma_rate(diag_report)
epsilon = epsilon_rate(diag_report)



O2_rating = parse(Int, oxygen_gen_rating(diag_report, gamma); base=2)
CO2_rating = parse(Int, CO2_scrub_rating(diag_report, epsilon); base=2)

print(O2_rating * CO2_rating)