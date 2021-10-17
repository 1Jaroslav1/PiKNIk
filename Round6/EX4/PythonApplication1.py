import pygame
import time

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()


def main():
    print('\nTURN UP THE VOLUME! ')
    print('Put a number bigger than 0, please: ')
    x=0
    while True:
        if(x==1):
            print('PUT A NUMBER BIGGER THAR 0 GENUIS!')
            play_sound("PiKNik/Round6/EX4/sounds/_bonk.mp3" , 0.3)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick()
        x=0
        try:
            size = int(input())
        except ValueError:
            print('PUT A NUMBER GENUIS!')
            play_sound("PiKNik/Round6/EX4/sounds/_minecraft_boo.mp3" , 1.5)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick()
        else: 
            if(size<=0):
                x=1
                continue
            break
    
    y=0
    f=0
    for i in range(1,size+1):
       if(i%3==0 and i%5!=0):
           print('Fizz')
           if(y==0):
               play_sound("PiKNik/Round6/EX4/sounds/_puk.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()  
           if(y==1):
               play_sound("PiKNik/Round6/EX4/sounds/_bababooey-sound-effect.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
           if(y==2):
               play_sound("PiKNik/Round6/EX4/sounds/_doctor.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
           continue 
       elif(i%3!=0 and i%5==0):
           print('Buzz')
           if(y==0):
               play_sound("PiKNik/Round6/EX4/sounds/_so_good.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           if(y==1):
               play_sound("PiKNik/Round6/EX4/sounds/_slay.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           if(y==2):
               play_sound("PiKNik/Round6/EX4/sounds/_burp.mp3" , 1)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           continue
       elif(i%3==0 and i%5==0):
           print('FizzBuzz')    
           if(y==2):
               play_sound("PiKNik/Round6/EX4/sounds/_ahah.mp3" , 5)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           elif(y==1):
               play_sound("PiKNik/Round6/EX4/sounds/_do_u_like.mp3" , 1.5)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           else:
               play_sound("PiKNik/Round6/EX4/sounds/_like_a_drum.mp3" , 2)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick()
           if(y!=3):
               y += 1
           else:
               y=0
           continue
       else:
           print(i)
           if(f==1):
               play_sound("PiKNik/Round6/EX4/sounds/_ah3.mp3" , 0.333)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==2):
               play_sound("PiKNik/Round6/EX4/sounds/_ah4.mp3" , 0.4)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==3):
               play_sound("PiKNik/Round6/EX4/sounds/_ah5.mp3" , 0.334)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==4):
               play_sound("PiKNik/Round6/EX4/sounds/_ah6.mp3" , 0.167)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==5):
               play_sound("PiKNik/Round6/EX4/sounds/_ah7.mp3" , 0.2)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==6):
               play_sound("PiKNik/Round6/EX4/sounds/_ah8.mp3" , 0.234)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==7):
               play_sound("PiKNik/Round6/EX4/sounds/_ah9.mp3" , 0.233)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==8):
               play_sound("PiKNik/Round6/EX4/sounds/_ah10.mp3" , 0.166)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==9):
               play_sound("PiKNik/Round6/EX4/sounds/_ah11.mp3" , 0.166)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==10):
               play_sound("PiKNik/Round6/EX4/sounds/_ah12.mp3" , 0.266)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==11):
               play_sound("PiKNik/Round6/EX4/sounds/_ah13.mp3" , 0.2)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           elif(f==12):
               play_sound("PiKNik/Round6/EX4/sounds/_ah14.mp3" , 0.133)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1
           else:
               f=0
               play_sound("PiKNik/Round6/EX4/sounds/_cupcakke_stony.mp3" , 0.5)
               while pygame.mixer.music.get_busy():
                   pygame.time.Clock().tick() 
               f+=1


main()