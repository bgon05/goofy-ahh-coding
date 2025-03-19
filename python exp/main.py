import pygame
import button
import spritesheet
import sys

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 467

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()
back_img = pygame.image.load('assets/back.png').convert_alpha()
background = pygame.image.load('assets/bg.png').convert_alpha()

sprite_sheet_image = pygame.image.load('assets/player-all-backup.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)

frame_0 = sprite_sheet.get_image(sprite_sheet_image, 0, 32, 32, 1.5, BLACK)
frame_1 = sprite_sheet.get_image(sprite_sheet_image, 1, 32, 32, 1.5, BLACK)
frame_2 = sprite_sheet.get_image(sprite_sheet_image, 2, 32, 32, 1.5, BLACK)
frame_3 = sprite_sheet.get_image(sprite_sheet_image, 3, 32, 32, 1.5, BLACK)
frame_4 = sprite_sheet.get_image(sprite_sheet_image, 4, 33, 32, 1.5, BLACK)
frame_5 = sprite_sheet.get_image(sprite_sheet_image, 5, 33, 32, 1.5, BLACK)

start_button = button.Button(SCREEN_WIDTH / 2 - 70, 200, start_img, 0.5)
exit_button = button.Button(SCREEN_WIDTH / 2 - 60, 300, exit_img, 0.5)
back_button = button.Button(10, 10, back_img, 0.5)
player = {
    "x": 0,
    "y": 390,
    "image": sprite_sheet_image
}

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
            
            screen.blit(frame_0, (0, 0))
            screen.blit(frame_1, (75, 0))
            screen.blit(frame_2, (150, 0))
            screen.blit(frame_3, (225, 0))
            screen.blit(frame_4, (300, 0))
            screen.blit(frame_5, (375, 0))

            # keys things
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                player['x'] -= 5
            elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                player['x'] += 5
            elif key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]:
                player['y'] -= 5

            # Prevent the player from moving off the screen
            if player["x"] < 0:
                player["x"] = 0
            if player["x"] + 32 > SCREEN_WIDTH:  # Assuming the player's width is 32
                player["x"] = SCREEN_WIDTH - 32
            if player["y"] < 0:
                player["y"] = 0
            if player["y"] + 32 > SCREEN_HEIGHT:  # Assuming the player's height is 32
                player["y"] = SCREEN_HEIGHT - 32
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

main()

pygame.quit()
sys.exit()
