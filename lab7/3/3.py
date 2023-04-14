import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

ball_radius = 25
ball_x = 400 // 2
ball_y = 300 // 2
ball_color = (255, 0, 0)

def draw_ball():
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

def is_off_screen():
    return ball_x < ball_radius or ball_x > 800 - ball_radius or ball_y < ball_radius or ball_y > 600 - ball_radius

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
    if not is_off_screen():
        screen.fill((255, 255, 255))  
        draw_ball()  
        pygame.display.update()
    pygame.time.Clock().tick(60)


