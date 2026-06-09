import pygame
from sys import exit
from pygamevideo import Video

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('LoR Dating Simulator')
clock = pygame.time.Clock()

pygame.font.init()

menuFont = pygame.font.Font("Fonts/Arita-buriM.otf", 60)

background = pygame.Surface((1920, 1080), pygame.SRCALPHA)
backgroundRect = background.get_rect(center = (1920/2, 1080/2))

quitButton = pygame.Surface((140,80), pygame.SRCALPHA)
quitButtonRect = quitButton.get_rect(center = (960, 930))
quitTxt = menuFont.render("Quit", True, (0,0,0))

playButton = pygame.Surface((140,80), pygame.SRCALPHA)
playButtonRect = playButton.get_rect(center = (960, 690))
playTxt = menuFont.render("Play", True, (0,0,0))

video = Video("Videos/[Video]TitleBackground_Loop.mp4")     #moving background for menu
video.play(loop=True)

while True:
    mousepos = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():    #Event system
        if event.type == pygame.QUIT:   #If you leave the game, close the game
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if quitButtonRect.collidepoint(mousepos):
                pygame.quit()
                exit()
            if playButtonRect.collidepoint(mousepos):
                print('Pressed play')

    video.draw_to(screen, (0, 0))       #load moving background

    screen.blit(quitTxt, quitButtonRect)
    screen.blit(playTxt, playButtonRect)
 
    pygame.display.flip()
    clock.tick(60)