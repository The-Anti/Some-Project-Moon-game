import pygame
from sys import exit
from pygamevideo import Video

pygame.init()

W=1920
H=1080

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('LoR Dating Simulator')
clock = pygame.time.Clock()

pygame.font.init()

menuFont = pygame.font.Font("Fonts/Arita-buriM.otf", 60)

background = pygame.Surface((1920, 1080), pygame.SRCALPHA)
backgroundRect = background.get_rect(center = (W/2, H/2))

quitButton = pygame.Surface((140,80), pygame.SRCALPHA)
quitButtonRect = quitButton.get_rect(center = (W/2, 930))
quitTxt = menuFont.render("Quit", True, (0,0,0))

playButton = pygame.Surface((140,80), pygame.SRCALPHA)
playButtonRect = playButton.get_rect(center = (W/2, 690))
playTxt = menuFont.render("Play", True, (0,0,0))

video = Video("Videos/[Video]TitleBackground_Loop.mp4")     #moving background for menu
video.play(loop=True)

testTextBox = pygame.Surface((1500, 300))
testTextBoxRect = testTextBox.get_rect(center = (W/2, H/1.2))
testTextBox.fill((200,200,200))

fadeToBlack = False
fadeIn = False
revert = False
tint = 0
start = False

count = 0

dialogue = ["", "And also test the dialogue iteration", "blah blah blah"]

def iterateDialogue(n):
    global text, textRect, revert, dialogue
    if n < len(dialogue):
        text = menuFont.render(dialogue[n], True, (0,0,0))
        textRect = text.get_rect(topleft = testTextBoxRect.topleft)

text = menuFont.render("Lets test this new textbox", True, (0,0,0))
textRect = text.get_rect(topleft = testTextBoxRect.topleft)

iteration = 0

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
                fadeToBlack = True
            if start:
                iteration += 1
                iterateDialogue(iteration)

    video.draw_to(screen, (0, 0))       #load moving background

    screen.blit(quitTxt, quitButtonRect)
    screen.blit(playTxt, playButtonRect)
 
    if fadeToBlack:
        background.fill((0,0,0))
        background.set_alpha(tint)
        tint+=5
        screen.blit(background, backgroundRect)
        if tint >= 255:
            start = True
            fadeToBlack = False
            quitButtonRect = quitButton.get_rect(center = (-960, -930))
            playButtonRect = playButton.get_rect(center = (-960, -690))

    if revert and tint > 0:
        background.set_alpha(tint)
        tint -= 5
        screen.blit(background, backgroundRect)
        if tint <= 0:
            revert = False
            tint = 0

    if start:
        screen.blit(testTextBox,testTextBoxRect)
        screen.blit(text, textRect)
        

    pygame.display.flip()
    clock.tick(60)
