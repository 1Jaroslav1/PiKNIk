import pygame
import time
import keyboard

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()



def main():
    print('Press any button to hear the sound')
    print('Press ESC to exit')
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('esc'):
                s='x'
                while s!='y' and s!='n':
                    print('  Are you sure you want to quit the program? y/n')
                    s=input()
                if(s=='y'):
                    break
                if(s=='n'):
                    print('Good choice!')
                    print('Press any button to hear the sound')
                    print('Press ESC to exit')
            if keyboard.is_pressed('3'):  
                play_sound("PiKNik/Round8/EX1/sounds/_bonk.mp3" , 0.3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('8'):  
                play_sound("PiKNik/Round8/EX1/sounds/_bonk.mp3" , 0.3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            
            if keyboard.is_pressed('q'):  
                play_sound("PiKNik/Round8/EX1/sounds/_bonk.mp3" , 0.3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('w'):
                play_sound("PiKNik/Round8/EX1/sounds/_minecraft_boo.mp3" , 1.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('e'):  
                play_sound("PiKNik/Round8/EX1/sounds/_puk.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('r'):   
                play_sound("PiKNik/Round8/EX1/sounds/_bababooey-sound-effect.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('t'):   
                play_sound("PiKNik/Round8/EX1/sounds/_doctor.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('y'):  
                play_sound("PiKNik/Round8/EX1/sounds/_so_good.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('u'):   
                play_sound("PiKNik/Round8/EX1/sounds/_slay.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('i'):  
                play_sound("PiKNik/Round8/EX1/sounds/_burp.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('o'):  
                play_sound("PiKNik/Round8/EX1/sounds/_ahah.mp3" , 5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('p'):  
                play_sound("PiKNik/Round8/EX1/sounds/_do_u_like.mp3" , 1.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('['):  
                play_sound("PiKNik/Round8/EX1/sounds/_like_a_drum.mp3" , 2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed(']'):  
                play_sound("PiKNik/Round8/EX1/sounds/_cupcakke_stony.mp3" , 0.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('a'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah3.mp3" , 0.333)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('s'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah4.mp3" , 0.4)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('d'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah5.mp3" , 0.334)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('f'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah6.mp3" , 0.167)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('g'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah7.mp3" , 0.2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('h'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah8.mp3" , 0.234)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('j'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah9.mp3" , 0.233)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('k'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah10.mp3" , 0.166)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('l'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah11.mp3" , 0.166)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed(';'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah12.mp3" , 0.266)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('\''):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah13.mp3" , 0.2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('z'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah14.mp3" , 0.133)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('x'):   
                play_sound("PiKNik/Round8/EX1/sounds/[WUT] Adam - original sound - wutadamyt.mp3" , 4)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('c'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah.mp3" , 9)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('v'):   
                play_sound("PiKNik/Round8/EX1/sounds/_cupcakke_stony.mp3" , 0.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('b'):   
                play_sound("PiKNik/Round8/EX1/sounds/_future.mp3" , 1.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('n'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ghoul.mp3" , 5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('m'):   
                play_sound("PiKNik/Round8/EX1/sounds/_krik.mp3" , 3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed(','):   
                play_sound("PiKNik/Round8/EX1/sounds/_panik_krik.mp3" , 5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('.'):   
                play_sound("PiKNik/Round8/EX1/sounds/_rofl_stony.mp3" , 2.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('/'):   
                play_sound("PiKNik/Round8/EX1/sounds/_shihiteo.mp3" , 3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('`'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah3.mp3" , 2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('1'):   
                play_sound("PiKNik/Round8/EX1/sounds/_smeh.mp3" , 2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('2'):   
                play_sound("PiKNik/Round8/EX1/sounds/_tear.mp3" , 11)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('4'):   
                play_sound("PiKNik/Round8/EX1/sounds/_bruh.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('5'):   
                play_sound("PiKNik/Round8/EX1/sounds/Sound_06372.mp3" , 3)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('6'):   
                play_sound("PiKNik/Round8/EX1/sounds/_doctor.mp3" , 2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('7'):   
                play_sound("PiKNik/Round8/EX1/sounds/_ah14.mp3" , 0.133)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('9'):   
                play_sound("PiKNik/Round8/EX1/sounds/_future.mp3" , 1.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('0'):   
                play_sound("PiKNik/Round8/EX1/sounds/_cupcakke_stony.mp3" , 0.5)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('-'):   
                play_sound("PiKNik/Round8/EX1/sounds/_slay.mp3" , 1)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
            if keyboard.is_pressed('='):   
                play_sound("PiKNik/Round8/EX1/sounds/_so_good.mp3" , 2)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick()
               
        except:
            print('Ups.. something happened. DONT TOUCH THIS BUTTON ANY MORE!')
            break  


main()
    
   