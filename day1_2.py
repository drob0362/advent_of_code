filename = 'input1'

with open(filename) as f:
    lines = f.readlines()

print(len(lines))
tup = tuple(lines)

halt_early = True
halt_index = 10

print(type(tup))
# capture measurements in a list
# clear group out when we've processed a block of 3
# find window of 3 using modulus
# store each group in a dict, as they may be required later
# dict usage dictname['key] or dictname = {'key1':value, 'key2':value}
# append to list = listname.append(value)
increase = 0
trioList = [];

for measurement_index in range(1, len(tup)):

    # print(measurement_index)
    next_measurement = int(tup[measurement_index])

    trioList.append(int(tup[measurement_index-1])) 

    if (measurement_index % 3 == 0):
        print("found end of window at pos {}".format(measurement_index))
        # capture list and reset
        print(trioList)
        trioList = [];



    next_measurement = int(tup[measurement_index])
    curr_measurement = int(tup[measurement_index-1])
    # print(type(curr_measurement))
    # print("is {0} > {1}".format(curr_measurement, next_measurement))
    if (next_measurement > curr_measurement):
        print("increase")
        increase = increase +1 

    if (halt_early and measurement_index == halt_index):
        print("halted at {} ".format(measurement_index))
        break

print("increased measurements = {0}".format(increase))
