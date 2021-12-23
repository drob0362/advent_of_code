import fnmatch, re
import sys
sys.path.append('../')

import read_file

tup = read_file.get_file_contents('input')
# print(len(tup))
# print(type(tup))
# print(tup)




# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

def get_readings_from_input(input):

    dist_re = re.compile("^forward")
    distance = list(filter(dist_re.match, input))
    # print(distance)

    depth_re = re.compile("^down|^up")
    depth = list(filter(depth_re.match, input))
    # print(depth)

    combined_readings = distance + depth
    print(combined_readings)
    return combined_readings

def create_list_of_dicts(list_arg):
    new_list = []
    for nested_list in list_arg:
        new_list.append(dict(zip(nested_list[::2], nested_list[1::2])))

    print(new_list)
    return new_list

def split_instruction_from_readings(input):
    new_list = []

    for reading in input:
        new_list.append(reading.split())

    print(new_list[0:5])
    return new_list

def calculate_final_depth(input_list_of_dicts):
    depth = 0
    for input_dict in input_list_of_dicts:
        dict_item_list = next(iter(input_dict.items()))
        # print(dict_item_list)
        if dict_item_list[0] == "up":
            # print("up")
            depth = depth - int(dict_item_list[1])
        elif dict_item_list[0] == "down":
            # print("down")
            depth = depth + int(dict_item_list[1])
    print("depth = {}".format(depth))
    return depth

def calculate_dist_travelled(input_list):
    dist = 0
    for input in input_list:
        dist = dist + int(input)

    print("horizontal distance = {}".format(dist))
    return dist

# horiz_pos_list = split_instruction_from_readings(horiz_pos_list, None)
# horiz_dist = calculate_dist_travelled(horiz_pos_list)

# readings = get_readings_from_input(tup)

split_instruction_from_readings(tup)

# depth_list = split_instruction_from_readings(None, depth_list)


# depth_list_of_dicts = convert_list_to_dict(depth_list)
# print(depth_list_of_dicts)
# depth = calculate_final_depth(depth_list_of_dicts)

# final_position = depth * horiz_dist
# print("final pos {}".format(final_position))

