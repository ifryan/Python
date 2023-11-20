import pandas as pd

csv = pd.read_csv('/Users/ryan/Downloads/finance.csv')
# print (csv[csv.columns[1]][1].index)



def findItem(item):
    indexNum = 0
    for i in csv[csv.columns[0]]:
        if item == i:
            return(indexNum)
        indexNum = indexNum + 1

def month(item):
    rowIndex = findItem(item)
    return(csv[csv.columns[1]][rowIndex])

def year(item):
    rowIndex = findItem(item)
    return(csv[csv.columns[2]][rowIndex])

def catalog(item):
    rowIndex = findItem(item)
    return(csv[csv.columns[3]][rowIndex])

def others(item):
    rowIndex = findItem(item)
    return(csv[csv.columns[4]][rowIndex])

print (month('千岛湖房租'))