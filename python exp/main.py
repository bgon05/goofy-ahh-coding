import pygame
import button
import player
import sys

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 467

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()
back_img = pygame.image.load('assets/back.png').convert_alpha()
background = pygame.image.load('assets/bg.png').convert_alpha()

start_button = button.Button(SCREEN_WIDTH / 2 - 70, 200, start_img, 0.5)
exit_button = button.Button(SCREEN_WIDTH / 2 - 60, 300, exit_img, 0.5)
back_button = button.Button(10, 10, back_img, 0.5)
player = player.Player((40, 40))

run = True

def menu():
    
    global run
    
    while run:
        pygame.display.set_caption('Menu')
        screen.fill((202, 228, 241))

        if start_button.draw(screen):
            main()

        if exit_button.draw(screen):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def main():
    global run
    in_menu = True

    while run:
        if in_menu:
            pygame.display.set_caption('Menu')
            screen.fill((202, 228, 241))

            if start_button.draw(screen):
                in_menu = False
                print('Start')

            if exit_button.draw(screen):
                run = False

        else:
            pygame.display.set_caption('Start')
            
            screen.blit(background, (0, 0))

            if back_button.draw(screen):
                in_menu = True
            
            screen.blit(player, (player.x, player.y))

            # keys things
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                player.move(-10, 0)
            elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                player.move(10, 0)
            elif key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]:
                player.move(0, -10)
            elif key[pygame.K_s] or key[pygame.K_DOWN]:
                player.move(0, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

main()

pygame.quit()
sys.exit()
