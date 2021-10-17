def find_max(tab):
    max = tab[0]
    for i in range(1, len(tab)):
        if not max[2]: max = tab[i]
        if max[2]:
            if max[1] < tab[i][1]: max = tab[i]

    return max


def main():
    wyniki = []
    n = int(input())

    for i in range(n):
        str = input().split(' ')
        sum = 0
        for j in range(1,6):
            sum += int(str[j])
        wyniki.append([str[0], sum, True])
    
    prev_res = [0, 0]
    # [l. punktow, wynik]
    for i in range(n):
        max = find_max(wyniki)
        wyniki[wyniki.index(max)][2] = False
        
        if prev_res[0] == max[1]: miejsce = prev_res[1]
        else: miejsce = i + 1

        prev_res = [max[1], miejsce]
        
        print(f'{miejsce}: {max[0]} {max[1]}')

if __name__ == '__main__':
    main()