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
    return digit_counter


def counter_to_binary(counts):
    binary_counter = []
    for i in counts:
        if i >= 0:
            binary_counter.append('1')
        else:
            binary_counter.append('0')
    return ''.join(binary_counter)


def binary_inverse(gamma):
    epsilon = []
    for digit in gamma:
        if digit == '1':
            epsilon.append('0')
        else:
            epsilon.append('1')
    return ''.join(epsilon)


gamma_rate = counter_to_binary(gamma_rate(number_list))

epsilon_rate = binary_inverse(gamma_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
