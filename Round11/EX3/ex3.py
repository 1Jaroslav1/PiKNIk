def convertInput(input):
    arr = []
    for elem in input:
        arr.append([ord(elem[0]) - 96, int(elem[1])])
    return arr


def main():
    first = input().split()
    second = input().split()

    convertedFirst = convertInput(first)
    convertedSecond = convertInput(second)

    combinations = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    for pos in convertedFirst:
        for combination in combinations:
            if pos[0] > 0 and pos[0] <= 8 and pos[1] > 0 and pos[1] <= 8:
                myX = pos[0] + combination[0]
                myY = pos[1] + combination[1]
                if myX > 0 and myX <= 8 and myY > 0 and myY <= 8:
                    for oponentPos in convertedSecond:
                        oponentX = oponentPos[0]
                        oponentY = oponentPos[1]
                        if oponentX == myX and oponentY == myY:
                            return "TAK"
            else:
                return "Błąd"
    
    return "NIE"

if __name__ == "__main__":
    ans = main()
    print(ans)