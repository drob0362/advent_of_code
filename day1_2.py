import sys

filename = 'input1'


def sumWindow(measurementList):
    print("in sumWindow")
    total = 0
    for measurement in measurementList:
        total = total + measurement
    print("total = {}".format(total))

# def compareWindows(window, measurementIndex):
#     # create next time window list


with open(filename) as f:
    lines = f.readlines()

print(len(lines))
tup = tuple(lines)

halt_early = True
halt_index = 10

# print(type(tup))
# capture measurements in a list
# clear group out when we've processed a block of 3
# find window of 3 using modulus
# store each group in a dict, as they may be required later
# dict usage dictname['key] or dictname = {'key1':value, 'key2':value}
# append to list = listname.append(value)
increase = 0
measurements = [];
measurementDict = {};
numWindows = 0;

#  need to compare 3 numbers (a) with next 3 numbers (b), with pos incr of 1 for b


# sys.exit(0)

for measurement_index in range(1, len(tup)):

    # we've reached a multiple of 3
    if (measurement_index % 3 == 0):
        print("found end of window at pos {}".format(measurement_index))
        trioList = [i for i in range(measurement_index-3, measurement_index)]
        print("window list = {} ".format(trioList))
        measurementDict[len(measurementDict)] = trioList


    if (halt_early and measurement_index == halt_index):
        print("halted at {} ".format(measurement_index))
        break

print("increased measurements = {0}".format(increase))

for i in range (len(measurementDict)):
    print("dictionary window list = {}".format(measurementDict[i]))



