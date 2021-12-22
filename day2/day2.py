import fnmatch, re
import sys
sys.path.append('../')

import read_file

tup = read_file.get_file_contents('input')
# print(len(tup))
# print(type(tup))
# print(tup)



def get_horizontal_positions(input):
    # print("*** horizontal positions")
    dist_re = re.compile("^forward")

    distance = list(filter(dist_re.match, input))
    # print(distance)
    return distance


def get_depth_readings(input):
    # print("**** depth readings")
    depth_re = re.compile("^down|^up")
    depth = list(filter(depth_re.match, input))
    # print(depth)
    return depth

def convert_list_to_dict(list_arg):
    new_list = []
    for nested_list in list_arg:
        new_list.append(dict(zip(nested_list[::2], nested_list[1::2])))

    print(new_list)

def split_instruction_from_readings(input_list):
    new_list = []
    for reading in input_list:
        new_list.append(reading.split())

    # print(new_list)
    return new_list

horiz_pos_list = get_horizontal_positions(tup)
horiz_pos_list = split_instruction_from_readings(horiz_pos_list)
depth_list = get_depth_readings(tup)
depth_list = split_instruction_from_readings(depth_list)


depth_list_of_dicts = convert_list_to_dict(depth_list)
print(depth_list_of_dicts)

