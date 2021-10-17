from random import random
from os import system

IND = ' ' * 5
COM = 'DOBRZE JEST ;)'
PLAY = True
BOMB = WIN = CC = False
WIDTH = HEIGH = SZANSA = 0
MENU = """\n--------MENU--------
1 -> Podaj wspolrzedne
2 -> Zakoncz gre"""

plansza = []

while(WIDTH < 2):
    WIDTH = int(input('Podaj szerokosc: '))
while(HEIGH < 2):
    HEIGH = int(input('Podaj wysokosc: '))
while(SZANSA <= 0.199999999999):
    SZANSA = float(input('Podaj szanse na bombe (w %): ')) / 100

system('cls')
#Initialize:
for i in range(HEIGH):
    plansza.append([])
    for j in range(WIDTH):
        x = random()
        if(x < SZANSA): x = 1
        else: x = 0

        plansza[i].append(x)

#Play loop
#PLANSZA:
# 0 - pusta ukryta
# 1 - bomba ukryta
# 2 - pusta wykryta
# 3 - bomba wykryta
# 4 - 
while(PLAY):
    system('cls')
    WIN = True
    print(COM)
    print(IND,end='   ')
    for i in range(WIDTH): print(i + 1,end=' ')
    print()
    # i - rzad
    # j - kolumna
    for i in range(HEIGH):
        print(IND, i + 1, end=' ')
        for j in range(WIDTH):
            z = plansza[i][j]
            if z == 0 or z == 1: 
                z = '#'
                WIN = False
            elif z == 2:
                c = 0
                x1 = x2 = 0
                
                if j != 0: x1 = j - 1
                else: x1 = 0
                if j != WIDTH - 1: x2 = j + 2
                else: x2 = WIDTH

                for l in range(x1,x2):
                    if i != 0:
                        if plansza[l][i - 1] == 1: c += 1
                    if plansza[l][i] == 1: c += 1
                    if i != HEIGH - 1:
                        if plansza[l][i + 1] == 1: c += 1
                # if c == 0:
                #     z = 'O'
                #     x1 = x2 = 0 

                #     if j != 0: x1 = j - 1
                #     else: x1 = 0
                #     if j != WIDTH - 1: x2 = j + 2
                #     else: x2 = WIDTH

                #     for l in range(x1,x2):
                #         if i != 0: plansza[l][i - 1] = 2
                #         plansza[l][i] = 2
                #         if i != HEIGH - 1: plansza[l][i + 1] = 2

                    # plansza[i][j] = 4
                    #CC = True

                    z = c

            elif z == 3: z = 'X'
            elif z == 4: z = 'O'
            print(z, end=' ')
        print()

    if BOMB:
        PLAY = False
        continue
    elif WIN:
        COM = 'WYGRALES! xD'
        BOMB = True
        continue
    elif CC:
        CC = False
        continue
    else: 
        print(MENU)
        ch = input("Zrob wybor: ")
        
    if ch == '1':
        x = abs(int(input('Podaj x: ')) - 1)
        y = abs(int(input('Podaj y: ')) - 1)
        COM = 'DOBRZE JEST ;)'
        if(x >= WIDTH or y >= HEIGH):
            COM = 'ZA DUZO, BYCZKU :|'
            continue
        z = plansza[y][x]

        if z == 0:
            plansza[y][x] = 2
        elif z == 1:
            plansza[y][x] = 3
            COM = 'PRZEGRALES, BYKU :('
            BOMB = True
    elif ch == '2':
        PLAY = False
    else: PLAY = False
