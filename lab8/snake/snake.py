import random
import pygame
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 400, 400
BLOCK_SIZE = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT+20))

clock = pygame.time.Clock()
font = pygame.font.SysFont(pygame.font.get_default_font(), 27)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#defines point (cells) on screen
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#class wall
class Wall:
    def __init__(self, level):
        self.body = []
        f = open("level{}.txt".format(level), "r")

        for y in range(0, HEIGHT/BLOCK_SIZE+1):
            for x in range(0, WIDTH/BLOCK_SIZE+1):
                if f.read(1) == "#":
                    self.bode.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * y, BLOCK_SIZE, BLOCK_SIZE )
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)





#defines body and head of snake on points
class Snake():
    def __init__(self):
        #initiating head
        self.body = [Point(x=WIDTH // BLOCK_SIZE // 2, y=HEIGHT // BLOCK_SIZE // 2,),]
        self.level = 1


    #draws body and head
    def draw(self):
        head = self.body[0]
        
        #draws head
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

        #draws body
        for body in self.body[1:]:
            pygame.draw.rect(SCREEN, BLUE, pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )


    #moves body after head
    def move(self, dx, dy):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        #finishes the game when snake bites itself
        for i in range(len(self.body) - 1, 0, -1):
            if self.body[i].x == self.body[0].x and self.body[i].y == self.body[0].y:
                game_over()

        #keeps snake in playing area
        if self.body[0].x > WIDTH // BLOCK_SIZE:
            game_over()
        elif self.body[0].x < 0:
            game_over()
        elif self.body[0].y < 0:
            game_over()
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            game_over()


    #checks if food is eaten
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True




class Food: #defines foods
    def __init__(self, x, y):
        self.location = Point(x, y)

    
    def draw(self): #draws food rectangles
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    

    def generate_new(self, snake_body):
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        #checks if food fell on snake's body, if true: generates again and checks from the beginning 
        for idx in range(len(snake_body) - 1, 0, -1):
            if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:
                self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                idx = len(snake_body) - 1



def draw_grid():
    #draw cells
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

    #draw borders
    pygame.draw.line(SCREEN, RED, start_pos=(0, HEIGHT-1), end_pos=(WIDTH-1, HEIGHT-1), width=1)  #bottom border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(0, HEIGHT), width=1)   #left border
    pygame.draw.line(SCREEN, RED, start_pos=(WIDTH-1, 0), end_pos=(WIDTH-1, HEIGHT-1), width=1)   #right border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(WIDTH, 0), width=1)    #top border 



def game_over():
    print("game over")
    sys.exit()




def main():

    running = True
    snake = Snake()
    food = Food(5, 5)
    wall = Wall(snake.level)
    dx, dy = 0, 0
    prev = 'none'
    score = 0
    level = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #prev - forbids going backwards if length   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and prev != 'down':
                    prev = 'up'
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and prev != 'up':
                    prev = 'down'
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT and prev != 'left':
                    prev = 'right'
                    dx, dy = +1, 0
                elif event.key == pygame.K_LEFT and prev != 'right':
                    prev = 'left'
                    dx, dy = -1, 0
                elif event.key == pygame.K_q:
                    running = False

        snake.move(dx, dy)

        #appending snake's body
        if snake.check_collision(food):
            score += 1
            level = score // 3

            food.generate_new(snake.body)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
        #levels
        if len(snake.body) > 4 and len(snake.body) %2 == 1:
            snake.level +=1
            wall = Wall(snake.level)
        
        #snake can go backwards if len == 1
        if len(snake.body) == 1: prev = 'none'

        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))

        SCREEN.fill(BLACK)
        SCREEN.blit(score_font, (0, HEIGHT))
        SCREEN.blit(level_font, (WIDTH // 2, HEIGHT))

        snake.draw()
        food.draw()
        draw_grid()

        pygame.display.flip()
        clock.tick(2 * level + 5)


if __name__ == '__main__':
    main()