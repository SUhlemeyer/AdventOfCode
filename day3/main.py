import sys
import os
import re
import numpy as np


def get_symbols(arr):
    chars = np.unique(arr)
    symbols = chars[(chars != '\n') & (chars != '.')]
    mask = np.isin(symbols, np.arange(10).astype('str'))
    symbols = symbols[~mask]
    return symbols

def get_numbers(arr):
    indices = []
    for i in range(arr.shape[0]):
        string = ''.join(map(str, arr[i,:]))
        indices_i = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', string)]
        indices.append(indices_i)
    return indices


def get_neighborhood(line, index, arr):
    nbh = arr[max(0, line-1):min(line+2, arr.shape[0]), max(0, index[0]-1):min(index[1]+1, arr.shape[1])]
    return nbh, max(0, line-1),  max(0, index[0]-1)

def get_arr(f):
    arr = []
    for line in f:
        line_list = []
        for char in line:
            line_list.append(char)
        if len(line_list) != 141:
            line_list.append('\n')
        arr.append(line_list)
    return np.array(arr)

def find_gear(arr):
    x, y = np.where(arr == '*')
    return x, y
            

def main():
    dir = sys.path[0]
    part_numbers = 0
    with open(os.path.join(dir, 'schematic.txt'), 'r') as f:
        arr = get_arr(f)

        symbols = get_symbols(arr)
        numbers = get_numbers(arr)
        gear_part_number_candidates = []
        gear_index_candidates = []
        gear_sum = 0
        
        for i, lst in enumerate(numbers):
            for index in lst:
                arr_, start_x, start_y = get_neighborhood(i, index, arr)
                nr = int(''.join(arr[i][index[0]:index[1]]))
                if np.sum(np.isin(arr_, symbols)) > 0:
                    part_numbers += nr
                if np.sum(np.isin(arr_, '*')) > 0:
                    gear_index = [start_x + np.where(arr_ == '*')[0], start_y + np.where(arr_ == '*')[1]]
                    if gear_index in gear_index_candidates:
                        ratio = gear_part_number_candidates[gear_index_candidates.index(gear_index)] * nr
                        gear_sum += ratio
                    else:
                        gear_index_candidates.append(gear_index)
                        gear_part_number_candidates.append(nr)
                    
    print("The sum of all part numbers is: ", part_numbers)
    print("The sum of all gear numbers is: ", gear_sum)

            
            

if __name__ == '__main__':
    main()