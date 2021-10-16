import pygame
import colorsys
from pynput.mouse import Button, Listener
import win32gui
import PySimpleGUI as sg

RGB = [0, 0, 0]

def pixel_color_at(x, y):
    hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    c = int(win32gui.GetPixel(hdc, x, y))
    # (r, g, b)
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff)

def on_click(x, y, button, pressed):
    if pressed and button == Button.right:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        global RGB
        RGB = pixel_color_at(x, y)
        print(RGB)
        return False

def drawTest(screen):
    pygame.draw.circle(screen, (255, 0, 0), (50, 20), 20)
    pygame.draw.circle(screen, (0, 255, 0), (100, 20), 20)
    pygame.draw.circle(screen, (0, 0, 255), (150, 20), 20)
    pygame.draw.circle(screen, (255, 0, 255), (200, 20), 20)
    pygame.draw.circle(screen, (255, 255, 0), (250, 20), 20)
    pygame.draw.circle(screen, (255, 155, 255), (300, 20), 20)
    pygame.draw.circle(screen, (100, 100, 255), (350, 20), 20)
    pygame.draw.circle(screen, (50, 50, 50), (400, 20), 20)
    # pygame.draw.rect(screen, pygame.Color((255, 0, 0)), pygame.Rect(20, 20, 20, 20))

def drawText(screen, string, pos, color):
    font = pygame.font.SysFont('arial', 15)
    label = font.render(string, 0.5, color)
    screen.blit(label, pos)

def getCMYK(r, g, b):
    r /= 255
    g /= 255
    b /= 255

    k = round(1 - max(r, g, b), 2)*100
    c = round((1-r-k)/(1-k), 2)*100
    m = round((1 - g - k)/(1-k), 2)*100
    y = round((1-b-k)/(1-k), 2)*100

    return (c, m, y, k)

def drawButton(screen):
    pygame.draw.rect(screen, pygame.Color((0, 0, 0)), pygame.Rect(50, 400, 150, 50))
    drawText(screen, "Button: Click LMB to activate", (50, 400), (255, 255, 255)) 
    pygame.draw.rect(screen, pygame.Color((255, 100, 0)), pygame.Rect(300, 400, 250, 150))
    drawText(screen, "Instruction", (300, 400), (255, 255, 255))
    drawText(screen, "1. Click LMB on button", (300, 430), (255, 255, 255)) 
    drawText(screen, "2. Click RMB anywhere to get color", (300, 460), (255, 255, 255))
 
def main():
    global RGB

    pygame.init()
    #listener.start()
    screen = pygame.display.set_mode((500, 500))

    running = True
    screen.fill((255, 255, 255))
    drawTest(screen)
    drawButton(screen)
    while running:
        for event in pygame.event.get():                
            [xPos, yPos] = pygame.mouse.get_pos()
            # [r, g, b, a] = screen.get_at((xPos, yPos))
            
            pygame.draw.rect(screen, pygame.Color(RGB), pygame.Rect(50, 100, 50, 50))
            pygame.draw.rect(screen, pygame.Color((255, 255, 255)), pygame.Rect(50, 150, 500, 500))
            drawText(screen, f"RGB: {RGB}", (50, 150), (0, 0, 0))
            drawText(screen, f"CMYK: {getCMYK(*RGB)}", (50, 200), (0, 0, 0))
            drawText(screen, f"HSV: {set(map(lambda x: round(x, 2), colorsys.rgb_to_hsv(*RGB)))}", (50, 250), (0, 0, 0))
            drawText(screen, f"HLS: {set(map(lambda x: round(x, 2), colorsys.rgb_to_hls(*RGB)))}", (50, 300), (0, 0, 0))
            drawText(screen, f"HEX: {'#%02x%02x%02x' % (RGB[0], RGB[1], RGB[2])}", (50, 350), (0, 0, 0))                              
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(xPos > 50 and yPos > 400 and xPos < 200 and yPos < 450):
                    listener = Listener(on_click=on_click)
                    listener.start()
            elif event.type == pygame.QUIT:
                running = False

        drawButton(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()