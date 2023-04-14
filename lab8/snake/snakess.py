import random
import pygame
import sys

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400 
WIDTH = 400
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)

BLOCK_SIZE = 20

#defines point (cells) on screen
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food: #defines foods
    def __init__(self):
        self.location = Point(4, 10)

    
    def draw(self): #draws food rectangles
        point = self.location
        pygame.draw.rect(SCREEN,RED,pygame.Rect(
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
#class wall            
class Wall:
    def __init__(self, level):
        self.body = []
        f = open("C:\erapp\pp2_KaliyevYerlan\lab8\snake\level{}.txt".format(level), "r")

        for y in range(0, HEIGHT//BLOCK_SIZE+1):
            for x in range(0, WIDTH//BLOCK_SIZE+1):
                if f.read(1) == "#":
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE )
            pygame.draw.rect(SCREEN, (PURPLE), rect)

    
#class snake
class Snake():
    def __init__(self):
        #initiating head
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1


    #draws body and head
    def draw(self):
        point = self.body[0]
        
        #draws head
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(
                point.x * BLOCK_SIZE,
                point.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

        #draws body
        for point in self.body[1:]:
            pygame.draw.rect(SCREEN, BLUE, pygame.Rect(
                    point.x * BLOCK_SIZE,
                    point.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )


    #moves body after head
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        #keeps snake in playing area
        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = HEIGHT // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0


    #checks if food is eaten
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
# draws grid
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT+20))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    font = pygame.font.Font(None, 27)
    snake = Snake()
    food = Food()
    wall = Wall(snake.level)
    score = 0
    newlevel = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    prev = 'up'
                    snake.dx, snake.dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    prev = 'down'
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_RIGHT:
                    prev = 'right'
                    snake.dx, snake.dy = +1, 0
                elif event.key == pygame.K_LEFT:
                    prev = 'left'
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_q:
                    pygame.quit()
        
        snake.move()
        #appending snake's body
        if snake.check_collision(food):
            score += 1
            food.generate_new(snake.body)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))

        #levels
        if len(snake.body) > 4 and len(snake.body) %2 == 1:
            newlevel = snake.level + 1
            snake = Snake()
            snake.level = newlevel
            wall = Wall(snake.level)
        
        #displays score and level
        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(newlevel), True, (255, 255, 255))

        SCREEN.fill(BLACK)
        SCREEN.blit(score_font, (0, HEIGHT))
        SCREEN.blit(level_font, (WIDTH // 2, HEIGHT))
        snake.draw()
        food.draw()
        wall.draw()

        draw_grid()

        pygame.display.update()
        CLOCK.tick(5)
        
main()