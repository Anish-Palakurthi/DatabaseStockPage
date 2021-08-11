def slimDate(datesArray):  # removes trailing zeros on datetime values
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


def fillZeros(integer):  # formats single digits months and days to have a leading zero for API call
    sInt = str(integer)
    sInt = sInt.zfill(2)
    return(sInt)


def testFunction():
    print("files are connected")
