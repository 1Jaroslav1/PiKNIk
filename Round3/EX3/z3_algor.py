def get_points(N):
    arr =[]

    for i in range(N):
        print(f'Podaj wspolrzedne punktu {i + 1} (Rozdzeilone spacja!)')
        
        temp = input().split(' ')
        x = int(temp[0])
        y = int(temp[1])

        arr.append([x, y])

    return arr
    
def get_field(arr):
    sum1 = sum2 = 0
    arr.append(arr[0])

    for i in range(len(arr) - 1):
        sum1 += arr[i][0] * arr[i + 1][1]
        sum2 += arr[i][1] * arr[i + 1][0]

    sum = (sum1 - sum2) / 2

    return abs(sum)

def colsion_check(lane1, lane2):
    #format: lane[point1, point2]
    #format: lane[[x1, y1], [x2, y2]]
    a1 = a2 = b1 = b2 = px = py = 0
    vert1 = vert2 = False

    print(f'lane1 = {lane1}\nlane2 = {lane2}')

    if lane1[0][0] is not lane1[1][0]:
        a1 = (lane1[0][1] - lane1[1][1])/(lane1[0][0] - lane1[1][0])
        b1 = lane1[0][1] - a1 * lane1[0][0]
    else: vert1 = True

    if lane2[0][0] is not lane2[1][0]:
        a2 = (lane2[0][1] - lane2[1][1])/(lane2[0][0] - lane2[1][0])
        b2 = lane2[0][1] - a2 * lane2[0][0] 
    else: vert2 = True

    if(a2 == a1): return False

    if vert1 and vert2:
        return False
    elif vert1:
        py = a2 * lane1[0][0] + b2
    elif vert2:
        py = a1 * lane2[0][0] + b1
    else:
        px = (b1 - b2) / (a2 - a1)
        if ((px > min(lane1[0][0], lane1[1][0]) and px < max(lane1[0][0], lane1[1][0])) or
            (px > min(lane2[0][0], lane2[1][0]) and px < max(lane2[0][0], lane2[1][0]))):
                return True

    if vert1 or vert2:
        if ((py > min(lane1[0][1], lane1[1][1]) and py < max(lane1[0][1], lane1[1][1])) or
            (py > min(lane2[0][1], lane2[1][1]) and py < max(lane2[0][1], lane2[1][1]))):
                return True

    return False


def points_check(arr):
    length = len(arr)

    for i in range(length):
        for j in range(i + 1,length):
            if(arr[i][0] == arr[j][0] and
                arr[i][1] == arr[j][1]): return False

    arr.append(arr[0])
    length = len(arr)
    for i in range(length - 3):
        for j in range(i + 2, length - 1):
            if colsion_check([arr[i], arr[i + 1]], [arr[j], arr[j + 1]]): return False
            #print(f'arr[i]: {arr[i]}\narr[j]: {arr[j]}')

    return True

def main():
    print('podaj liczbe punktow: ')
    N = int(input())
    
    punkty = get_points(N)
    #print(punkty)

    if(not points_check(punkty)):
        return 'Blad!'
    
    pole = get_field(punkty)

    return(pole)

if __name__ == '__main__':
    print(main())