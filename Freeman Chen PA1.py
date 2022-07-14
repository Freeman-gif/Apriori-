from apyori import apriori
import pandas as pd
##read txt
def readfile():
    datalist = []
    with open('browsingdata.txt') as inputfile:
        for line in inputfile:
            datalist.append(line.strip().split(' '))
    return datalist

datalist = readfile()


def run(datalist):
    basket = len(datalist)
    output = open("output.txt", 'w')
    baskets = len(datalist)##find how many baskets are there
    result = (apriori(datalist, min_support= 100/baskets))
    Pair = {} ##paris of frozen set
    Trip = {} ##
    for data in result:
        if((len(data[0]))) == 2:
            joinpairs = " ".join(list(data[0]))
            Pair[joinpairs] = data[1]  # Populating the dictionary to be sorted later
        elif (len(list(data[0]))) == 3:  # Same process for pairs
            jointrips = " ".join((list(data[0])))
            Trip[jointrips] = data[1]
    # create alist of tuples with paris and trip and sort the confidence with decsnding order.
    SortedPairs = sorted(Pair.items(), key=lambda x: x[1], reverse=True)
    SortedTrips = sorted(Trip.items(), key=lambda x: x[1], reverse=True)

    #limit both loops only print the top 5 confidence item
    count = 0
    output.write("Output A:\n")
    for(pair, confidence) in SortedPairs:
        count += 1
        if count >5:
            break
        else:
            output.write(pair)
            output.write(" ")
            output.write(str(confidence))
            output.write("\n")
    output.write("Output B:\n")
    countTrip = 0
    for(trip, confidence) in SortedTrips:

        countTrip += 1
        if countTrip >5:
            break
        else:
            output.write(trip)
            output.write(" ")
            output.write(str(confidence))
            output.write("\n")
    output.close()


if __name__ =="__main__":
    run(datalist)



