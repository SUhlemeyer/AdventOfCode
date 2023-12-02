import sys
import os
import re


def get_game_id(line):
    game = line.split(':')[0]
    return int(''.join(c for c in game if c.isdigit()))


def find_max(color, line):
    rounds = line.split(':')[-1]
    numbers = re.findall(r"(\d+) {}".format(color), rounds)
    max_number = max([int(i) for i in numbers])
    return max_number
            

def main():
    dir = sys.path[0]
    bag = {'red': 12, 'green': 13, 'blue': 14}
    valid_id_sum = 0
    power_sum = 0
    
    with open(os.path.join(dir, 'game.txt'), 'r') as f:
        for line in f:
            game_id = get_game_id(line)
            possible = True
            power = 1
            for k, v in bag.items():
                max_color = find_max(k, line)
                power *= max_color
                if max_color > v:
                    possible = False
            power_sum += power
            if possible:
                valid_id_sum += game_id
    print("The sum of IDs of possible games is: ", valid_id_sum)
    print("The sum of game powers is: ", power_sum)



if __name__ == '__main__':
    main()