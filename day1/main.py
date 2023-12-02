import sys
import os
import re


def get_calibration_value(line):
    new_line = transform_digits(line)
    digits = ''.join(c for c in new_line if c.isdigit())
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)


def transform_digits(line):
    digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    start_positions = []
    digits = []
    for k, v in digit_dict.items():
        indices = [m.start() for m in re.finditer(k, line)]
        for ind in indices:
            start_positions.append(ind)
            digits.append(v)
    for pos, digit in enumerate(digits):
        line = line[:start_positions[pos]] + digit + line[start_positions[pos]+1:]
        
    return line


def main():
    dir = sys.path[0]
    cal_values = 0
    with open(os.path.join(dir, 'calibration.txt'), 'r') as f:
        for line in f:
            digit = get_calibration_value(line)
            cal_values += digit
    print("The sum of calibration values is: ", cal_values)


if __name__ == '__main__':
    main()