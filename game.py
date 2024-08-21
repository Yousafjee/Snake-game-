import pygame
pygame.init()

# Creating Windows
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False

# Creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("You have pressed right arrow key")

pygame.quit()
quit()

