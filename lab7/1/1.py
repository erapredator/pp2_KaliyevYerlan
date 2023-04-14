import pygame
import datetime
import math

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab7\1\mickeyclock.jpg")
left_hand = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab7\1\left_hand.png").convert_alpha()
right_hand = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab7\1\right_hand.png").convert_alpha()

lh_rect = left_hand.get_rect()
lh_rect.center = screen.get_rect().center

rh_rect = right_hand.get_rect()
rh_rect.center = screen.get_rect().center


image = pygame.transform.scale(image, (width, height))
left_hand = pygame.transform.scale(left_hand, (width-150, height-150))
right_hand = pygame.transform.scale(right_hand, (width-200, height-200))



clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = -minute * 6
    second_angle = -second * 6



    left_hand_rotated = pygame.transform.rotate(left_hand, second_angle)
    left_hand_rotated_rect = left_hand_rotated.get_rect(center=lh_rect.center)

    right_hand_rotated = pygame.transform.rotate(right_hand, minute_angle)
    right_hand_rotated_rect = right_hand_rotated.get_rect(center=rh_rect.center)



    screen.fill((255, 255, 255))
    
    screen.blit(image, (0, 0))
    screen.blit(left_hand_rotated, left_hand_rotated_rect)
    screen.blit(right_hand_rotated, right_hand_rotated_rect)


    
    txt = str(minute) + " : " + str(second)
    time_text = font.render(txt, True, (0, 0, 0))
    screen.blit(time_text, (350, 25))
    pygame.display.flip()
    clock.tick(60)