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

sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()
text_surface = test_font.render("Gamey game time!",False,'Red')

snail_surf = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf, player_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800   
    

    # if player_rect.colliderect(snail_rect):
    #     player_rect.x -= 40

    # if player_rect.right <= 0:
    #     player_rect.x = 300
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())

    #player_rect.x += 1
    pygame.display.update()
    clock.tick(60)