import pygame
import time

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()

g='x'
age=0
gr=0
w=0
while True:
    print('Gender m/w: ')
    g=input()
    if(g=='m' or g=='w'):
        break
    play_sound("PiKNik/Round11/EX5/_bonk.mp3" , 0.3)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

while True:
    try:
        print('Age 18+: ')
        age = int(input())
        if(age<18): 
            continue
        if(age>=18):
            break
    except ValueError:
        print('PUT A NUMBER GENUIS!')
        play_sound("PiKNik/Round11/EX5/_bonk.mp3" , 0.3)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick()


while True: 
    try:
        print('How much did you drink? (grams): ')
        gr = int(input())
        if(gr<=0): 
            print('PUT A NUMBER BIGGER THAR 0 GENUIS!')
            play_sound("PiKNik/Round11/EX5/_bonk.mp3" , 0.3)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick()
            continue
        if(gr>0):
            break
    except ValueError:
        print('PUT A NUMBER GENUIS!')
        play_sound("PiKNik/Round11/EX5/_bonk.mp3" , 0.3)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick()
print('Name of drink: ')
d=input()

while True: 
    try:
        print('Your weight?(kg): ')

        w = int(input())
        if(w<=0): 
            print('PUT A NUMBER BIGGER THAR 0 GENUIS!')
            continue
        if(w>0):
            break
    except ValueError:
        print('PUT A NUMBER GENUIS!')
        play_sound("PiKNik/Round11/EX5/_bonk.mp3" , 0.3)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick()
Q=0
if(g=='w'):
    Q=gr/(w*0.6)
if(g=='m'):
    Q=gr/(w*0.7)
if(Q<=0.2):
    print(Q,'%   YOU CAN DRIVE!')
    play_sound("PiKNik/Round11/EX5/_cupcakke_stony.mp3" , 0.8)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()
if(Q>0.2):
    j=0
    if(g=='w'):
        j=0.2/0.1
    if(g=='m'):
        j=0.2/0.15
    print(Q,'%  NO YOU CANT DRIVE! ITS POSSIBLE IN',j,'HOURS!')
    play_sound("PiKNik/Round11/EX5/_ah2.mp3" , 0.5)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()