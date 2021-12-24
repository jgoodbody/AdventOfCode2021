#!/usr/bin/env python3

with open('input.txt') as f:
    numbers = f.read().splitlines()

number_list = []
for num in numbers:
    number_list.append(num)


def gamma_rate(report):
    digit_counter = [0] * len(report[0])
    for num in report:
        for place, digit in enumerate(num):
            if digit == '1':
                digit_counter[place] += 1
            else:
                digit_counter[place] -= 1
    binary_counter = []
    for i in digit_counter:
        if i >= 0:
            binary_counter.append('1')
        else:
            binary_counter.append('0')
    return ''.join(binary_counter)


def epsilon_rate(report):
    digit_counter = [0] * len(report[0])
    for num in report:
        for place, digit in enumerate(num):
            if digit == '1':
                digit_counter[place] += 1
            else:
                digit_counter[place] -= 1
    binary_counter = []
    for i in digit_counter:
        if i >= 0:
            binary_counter.append('0')
        else:
            binary_counter.append('1')
    return ''.join(binary_counter)


def oxygen_gen_rating(report, most_common):
    length = len(report)
    filtered = report[:]
    for i in range(length):
        for index, num in enumerate(filtered):
            if num[i] != most_common[i]:
                filtered[index] = None
        filtered = list(filter(None, filtered))
        length = len(filtered)
        most_common = gamma_rate(filtered)
        if length == 1:
            return filtered[0]
    return most_common


def CO2_scrub_rating(report, least_common):
    length = len(report)
    filtered = report[:]
    for i in range(length):
        for index, num in enumerate(filtered):
            if num[i] != least_common[i]:
                filtered[index] = None
        filtered = list(filter(None, filtered))
        length = len(filtered)
        least_common = epsilon_rate(filtered)
        if length == 1:
            return filtered[0]
    return least_common


O2_rating = int(oxygen_gen_rating(number_list, gamma_rate(number_list)), 2)
CO2_rating = int(CO2_scrub_rating(number_list, epsilon_rate(number_list)), 2)

print(O2_rating * CO2_rating)
