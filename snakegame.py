import pygame
pygame.init()
import random
import os

pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Creating Windows
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background Image
bgimg1 = pygame.image.load("image1.jpg")
bgimg2 = pygame.image.load("image2.jpg")

bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("My First Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
 

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list: 
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(bgimg1, (0,0))
        text_screen("Welcome to Snake Game", white, 215, 240)
        text_screen("Press Space Bar To Play", white, 225, 280)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('music.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Creating game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_lenght = 1


    # Load food sound
    food_sound = pygame.mixer.Sound('food.mp3')

    #  Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w")as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore =int(f.read())

    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))
    score  = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)

            text_screen("Game Over! Press Enter to Continue", red, 100, 250)
            text_screen("Your Score: " + str(score), green, 310, 290)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP: 
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                score += 10
                food_x = random.randint(20, int(screen_width / 2))
                food_y = random.randint(20, int(screen_height / 2))
                snk_lenght +=5
                # Play food sound without stopping the background music
                food_sound.play()

            if score>int(hiscore): 
                hiscore = score


            gameWindow.blit(bgimg2, (0,0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), white, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]



            if head in snk_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

