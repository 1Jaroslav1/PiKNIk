import pygame
import time
import math

from pygame.mixer import pause

buttonColor = [70, 70, 70]

def drawText(screen, string, pos, color):
    font = pygame.font.SysFont('arial', 25)
    label = font.render(string, 0.5, color)
    screen.blit(label, pos)

def play_sound(source, stime=0.08):
    pygame.mixer.init()
    pygame.mixer.music.load(source)
    pygame.mixer.music.play()
    time.sleep(stime)

    pygame.mixer.music.stop()

class Button:
    def __init__(self, text, pos, size):
        self._text = text
        self._pos = pos
        self._size = size
        self._sound = "PiKNik/Round5/EX1/Click2.mp3"
    
    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        self._size = new_size
        
    def draw(self, display):
        pygame.draw.rect(display, pygame.Color(buttonColor), pygame.Rect(self._pos[0], self._pos[1], self._size[0], self._size[1]))
        drawText(display, self._text, [self._pos[0] + self._size[0] // 3, self._pos[1] + self._size[1]//3], [0, 255, 255])
        pygame.display.update()

    def check_click(self):
        click_pos = pygame.mouse.get_pos()

        if click_pos[0] <= self._pos[0] or click_pos[0] >= (self._pos[0] + self._size[0]) or click_pos[1] <= self._pos[1] or click_pos[1] >= (self._pos[1] + self._size[1]):
            return False
        play_sound(self._sound, 0.22)
        return True

def getTerminalTime():
    return int(input("Give time in secunds: "))

def getSoundSorce():
    return input("Give source of sound(pres d for default sound): ")

def drawTime(mainTime, screen, pos):
    time = math.floor(mainTime)
    text = f"{((time // 60)//60)%24:02} : {(time // 60)%60:02} : {time % 60:02}"
    pygame.draw.rect(screen, pygame.Color([146, 146, 140]), pygame.Rect(pos[0], pos[1], 200, 50))
    drawText(screen, text, pos, [255, 255, 255])

def timeUpdate(inputTime, startTime, pauseTime):
    return inputTime - (time.time() - startTime - pauseTime)

def main():
    inputTime = getTerminalTime()
    source = getSoundSorce()
    mainTime = inputTime

    startTime = 0
    pauseTime = 0
    pauseStart = 0

    pygame.init()
    screen = pygame.display.set_mode((500, 250))

    running = True
    startClicked = False
    pauseClicked = False

    screen.fill((146, 146, 140))
    start_button = Button("Start", [50, 50], [120, 50])
    pause_button = Button("Stop", [50, 120], [120, 50])

    start_button.draw(screen)
    pause_button.draw(screen)

    mainStartClicked = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_click() and not startClicked:
                    if not mainStartClicked:
                        startTime = time.time()
                        mainStartClicked = True

                    startClicked = True
                    pauseClicked = False
                    if pauseStart > 0:
                        pauseTime += time.time() - pauseStart
                        pauseStart = 0

                elif pause_button.check_click() and not pauseClicked:
                    pauseStart = time.time()
                    pauseClicked = True
                    startClicked = False

            elif event.type == pygame.QUIT:
                running = False

        start_button.draw(screen)
        pause_button.draw(screen)

        if startTime > 0:
            if startClicked:
                mainTime = timeUpdate(inputTime, startTime, pauseTime)
                drawTime(mainTime, screen, [250, 100])
        else:
            drawTime(inputTime, screen, [250, 100])
        
        if mainTime <= 0:
            drawTime(0, screen, [250, 100])
            if source == "d":
                play_sound("PiKNik/Round5/EX1/ACDC – If You Want Blood.mp3" , 15)
            else:
                play_sound(source , 15)
            running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()