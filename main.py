import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player walk 1 and 2 does not get self keyword as they don't need acceccing outside of the init method
        player_walk_1 = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics\Player\player_walk_2.png').convert_alpha()
        self.player_walk =[player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics\Player\jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio\jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210

        else:
            snail_frame_1 = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics\snail\snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.speed = 5
        self.image = self.frames[self.animation_index] 
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))          
                                                                                            
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.destroy()
        # print(pygame.time.get_ticks() - start_time)
        # if (pygame.time.get_ticks() - start_time) % 5000 == 0:
        # # if score % 5 == 0:
        #     print("Score: " + str(score))
        #     self.speed += int(self.speed*1.10)
        print("Speed: "+ str(self.speed))
        self.rect.x -= self.speed
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - int(start_time/1000)
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,40))
    screen.blit(score_surface,score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()
#initialize Display Surface (main poster)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
# background_music = pygame.mixer.Sound('audio\music.wav')
background_music = pygame.mixer.Sound('audio\grabbag.mp3')
background_music.set_volume(1)
background_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

#Intro screen
player_stand = pygame.image.load("graphics\Player\player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

header_text_surface = test_font.render(f'Pixel Runner', False, (111,196,169))
header_text_rect = header_text_surface.get_rect(center = (400,60))

footer_text_surface = test_font.render(f'Press spacebar to run', False, (111,196,169))
footer_text_rect = footer_text_surface.get_rect(center = (400,350))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

speed_increment_timer = pygame.USEREVENT + 2
pygame.time.set_timer(speed_increment_timer, 3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            #Obstacle Spawn Event
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            # if event.type == speed_increment_timer:
                # for obstacle in obstacle_group:
                #     obstacle.speed += 1
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
    if game_active:
        #Draw sky,ground and score to screen
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,300))
        score = display_score()

        #Draw and update player
        player.draw(screen)
        player.update()

        #Draw and update obstacle 'sprites'
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        #Check Colisions:
        game_active = collision_sprite()

    else:
        #Display splash/start screen
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        screen.blit(header_text_surface,header_text_rect)
        score_message = test_font.render(f'Score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,350))

        if score == 0:
            screen.blit(footer_text_surface,footer_text_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)