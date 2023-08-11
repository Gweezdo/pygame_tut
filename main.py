import pygame
from sys import exit

pygame.init()
#initialize Display Surface (main poster)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 50)
#initialize 'regular' surface (stuff that goes onto poster)
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')

sky_surface = pygame.image.load('graphics\Sky.png')
ground_surface = pygame.image.load('graphics\ground.png')
text_surface = test_font.render("Gamey game time!",True,'Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))

    pygame.display.update()
    clock.tick(60)