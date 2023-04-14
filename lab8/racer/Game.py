# import necessary modules
import pygame, sys
from pygame.locals import *
import random, time
 
# Initialize pygame
pygame.init()
 
# Set frames per second
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Create colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Set up screen width, height, and speed
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
 
# Set up initial score and coins
SCORE = 0
COINS = 0
 
# Set up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
# Load background image and music
background_image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab8\racer\AnimatedStreet.png")
background_music = pygame.mixer.music.load(r'C:\erapp\pp2_KaliyevYerlan\lab8\racer\background.wav')
pygame.mixer.music.play()
 
# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
# Creating class of enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
    
    # Move enemy and update score if enemy goes off screen
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Creating class of coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab8\racer\Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
    
    # Move coin, update coin count if collected, and reset coin position if off screen
    def move(self):
        self.rect.move_ip(0,5)
        global COINS, coins_group
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        #Cheaks for collisio betwenn player and coin
        if pygame.sprite.spritecollideany(P1, coins_group):
            pygame.mixer.Sound(r'C:\erapp\pp2_KaliyevYerlan\lab8\racer\coinsound.mp3').play()
            COINS +=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
# Creating class of player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True: 
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.25     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #showing score and number of coins
    DISPLAYSURF.blit(background_image, (0,0))
    scores = font_small.render("Point " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coins = font_small.render("Coin " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (100,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #Cheaks for collision between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound(r'C:\erapp\pp2_KaliyevYerlan\lab8\racer\crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
    
    pygame.display.update()
    FramePerSec.tick(FPS)