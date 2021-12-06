# import sys

filename = 'input1'

increase = 0
measurementDict = {}
totalsDict = {}

def sumWindow(measurementList):
    total = 0
    for measurement in measurementList:
        total = total + int(measurement)
    print("measurement window total = {}".format(total))
    return total

def processMeasurements(measurementDict):

    increase = 0
    for i in range (1, len(measurementDict)):
        next_measurement = sumWindow(measurementDict[i])
        curr_measurement = sumWindow(measurementDict[i-1])

        if (next_measurement > curr_measurement):
            print("increase")
            increase = increase +1 
        # print("next m {}".format(next_measurement))
        # print("curr m {}".format(curr_measurement))
        # list retrieved from dictionary
        # print(type(measurementDict[i]))
        # call sumwindow on current entry and previous
        # then compare, as in script 1


with open(filename) as f:
    lines = f.read().splitlines()

# print(len(lines))
tup = tuple(lines)

halt_early = True
halt_index = 30

# print(type(tup))
# capture measurements in a list
# clear group out when we've processed a block of 3
# find window of 3 using modulus
# store each group in a dict, as they may be required later
# dict usage dictname['key] or dictname = {'key1':value, 'key2':value}
# append to list = listname.append(value)


#  need to compare 3 numbers (a) with next 3 numbers (b), with pos incr of 1 for b


# sys.exit(0)

for measurementIndex in range(1, len(tup)):

    # we've reached a multiple of 3
    if (measurementIndex % 3 == 0):
        intMeasurementIndex = int(measurementIndex)
        print("found end of window at pos {}".format(measurementIndex))
        trioList = [tup[i] for i in range(measurementIndex-3,
            measurementIndex)]
        # print("window list = {} ".format(trioList))
        measurementDict[len(measurementDict)] = trioList


    if (halt_early and measurementIndex == halt_index):
        print("halted at {} ".format(measurementIndex))
        break

print("increased measurements = {0}".format(increase))

# print measurement windows
for i in range (len(measurementDict)):
    print("dictionary window list = {}".format(measurementDict[i]))
    #  pass in list
    sumWindow(measurementDict[i])

# now calculate the increases from the dictionary measurements
processMeasurements(measurementDict)



