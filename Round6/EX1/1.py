import requests
import csv
import numpy as np
import matplotlib.pyplot as plt

# READ: if you don`t have files downloaded.csv and test.txt run saveData() and createNameFile()

def saveData():
    try:
        res = requests.get("https://raw.githubusercontent.com/fivethirtyeight/data/master/polls/pres_primary_avgs_1980-2016.csv")
        content = res.content

        csv_file = open('PiKNik/Round6/EX1/downloaded.csv', 'wb')

        csv_file.write(content)
        csv_file.close()

    except Exception as e:
        print("Error")

def getData():
    rows = []
    with open('PiKNik/Round6/EX1/downloaded.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return rows

def createNameFile():
    rows = getData()
    
    names = []
    for row in rows:
        name = row[3]
        if not name in names:
            names.append(name)
    
    with open("PiKNik/Round6/EX1/test.txt", "w") as txt_file:
        for row in names:
            txt_file.write(row + "\n")

def getDataTxt():
    with open("PiKNik/Round6/EX1/test.txt", "r") as txt_file:
        names = txt_file.read().splitlines()
    return names

def main():
    rows = getData()
    names = getDataTxt()

    getName = False
    print(names)
    while not getName:
        inputName = input("Write name to get statistic: ")
        if inputName in names:
            getName = True
        else:
            print("Choose name from list")
            print(names)

    candidateDict = {}
    for row in rows:
        if row[3] == inputName:
            if row[1] in candidateDict:
                candidateDict[row[1]] += 1
            else:
                candidateDict[row[1]] = 1

    x = np.arange(len(candidateDict))
    values = list(map(lambda x: x//9, candidateDict.values()))
    plt.bar(x, height=values)
    plt.xticks(x, list(candidateDict.keys()), rotation=70)

    plt.xlabel('States')
    plt.ylabel('Average number of votes of 36 years')
    plt.title(inputName)

    plt.show()


if __name__ == "__main__":
    main()