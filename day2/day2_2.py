import fnmatch, re
from os import read
import sys
sys.path.append('../')

import read_file

tup = read_file.get_file_contents('sample_input')
# print(len(tup))
# print(type(tup))
# print(tup)

horiz_pos = 0
aim = 0
depth = 0

def split_instruction_out(input):
    readings_list = []
    for input_line in input:
        readings_list.append(input_line.split())

    return readings_list

def convert_list_to_dict(list_arg):
    new_list = []
    for nested_list in list_arg:
        print(nested_list)
        print(nested_list[::2])
        # new_list.append(dict(zip(nested_list[::2], nested_list[1::2])))

    # print(new_list)
    return new_list


def identify_instruction(instruction):

    global horiz_pos, aim, depth

    if instruction[0] == 'forward':
        process_forward(horiz_pos, depth, aim, instruction[1])
    else:
        aim =  aim + adjust_aim(instruction)
        print("aim = {}".format(aim))


def adjust_aim(reading_input):
    print("direction is {}, aim adjust is {}".format(reading_input[0], reading_input[1]))
    if reading_input[0] == 'down':
        return - int(reading_input[1])
    # must be up
    return int(reading_input[1])

# TODO complete forward calculations
def process_forward(horizontal_pos, depth, aim, reading):
    print("forward distance = {}".format(reading))
    horizontal_pos = horizontal_pos + int(reading)
    depth = (depth * aim) * reading
    print("depth = {}".format(depth))
    return depth

readings_list = split_instruction_out(tup)
print(readings_list)

count = 0
for reading in readings_list:
    identify_instruction(reading)
    count = count + 1
    if count == 10:
        break

print("aim = {}, depth = {}".format(aim, depth))