# removes trailing zeros on datetime array
def slimDate(datesArray):
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


# formats single digits months and days to have a leading zero for API call (8 -> 08)
def fillZeros(integer):
    sInt = str(integer)
    sInt = sInt.zfill(2)
    return(sInt)
