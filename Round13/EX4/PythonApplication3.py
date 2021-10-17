import pygame
import time
import keyboard
import webbrowser

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()


def main():
    print('\n\n NEVER GONNA GIVE YOU UP? y/n')
    z=input()
    webbrowser.open_new('https://rickrollhurban.carrd.co/')
    play_sound("PiKNik/Round13/EX4/music.mp3" , 213)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

main()