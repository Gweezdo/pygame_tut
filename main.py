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

score_surf = test_font.render("Score!",False,(64,64,64))
score_rect = score_surf.get_rect(center = (screen.get_width()/2 , 50))
print(screen.get_width()/2)

snail_surf = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen,'#c038ec',score_rect)
    pygame.draw.rect(screen,'#c038ec',score_rect, 10)

    #pygame.draw.line(screen,"Red",(0,0),pygame.mouse.get_pos())
    #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

    screen.blit(score_surf, score_rect)
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf, player_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800   
    

    # if player_rect.colliderect(snail_rect):
    #     player_rect.x -= 40

    # if player_rect.right <= 0:
    #     player_rect.x = 300
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    #player_rect.x += 1
    pygame.display.update()
    clock.tick(60)