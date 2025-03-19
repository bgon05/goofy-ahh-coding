import pygame
import button
import spritesheet
import sys

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()
back_img = pygame.image.load('assets/back.png').convert_alpha()
#background = pygame.image.load('assets/bg.png').convert_alpha()
background2 = pygame.image.load('assets/image.png').convert_alpha()

sprite_sheet_image = pygame.image.load('assets/player-pos1.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)
gravity = 0.5
y_velocity = 0
jump_strength = -10

frame_0 = sprite_sheet.get_image(sprite_sheet_image, 0, 32, 32, 1.5, BLACK)
frame_1 = sprite_sheet.get_image(sprite_sheet_image, 1, 32, 32, 1.5, BLACK)
frame_2 = sprite_sheet.get_image(sprite_sheet_image, 2, 32, 32, 1.5, BLACK)
frame_3 = sprite_sheet.get_image(sprite_sheet_image, 3, 32, 32, 1.5, BLACK)
frame_4 = sprite_sheet.get_image(sprite_sheet_image, 4, 33, 32, 1.5, BLACK)
frame_5 = sprite_sheet.get_image(sprite_sheet_image, 5, 33, 32, 1.5, BLACK)

platform = pygame.draw.rect(screen, BLACK, (50, 350, 50, 10))

start_button = button.Button(SCREEN_WIDTH / 2 - 70, 200, start_img, 0.5)
exit_button = button.Button(SCREEN_WIDTH / 2 - 60, 300, exit_img, 0.5)
back_button = button.Button(10, 10, back_img, 0.5)
#player logic
sprite_sheet_image = {
    "x": 0,
    "y": 390,
}

#platform logic
platforms = [
    {'x': 50, 'y': 350, 'width': 100, 'height': 10},
    {'x': 200, 'y': 300, 'width': 150, 'height': 10},
    {'x': 400, 'y': 250, 'width': 200, 'height': 10},
    {'x': 650, 'y':200, 'width': 250, 'height': 10},
]

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
    global run, y_velocity
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
            
            screen.blit(background2, (0, 0))
            #screen.blit(background, (0, 0))
            #screen.fill(BLACK)

            if back_button.draw(screen):
                in_menu = True

            #gravity
            y_velocity += gravity
            sprite_sheet_image['y'] += y_velocity

            for platform in platforms:
                platform_x = platform['x']
                platform_y = platform['y']
                platform_width = platform['width']
                platform_height = platform['height']

                if (
                    sprite_sheet_image['x'] + 48 > platform_x and  # Player's right edge > platform's left edge
                    sprite_sheet_image['x'] < platform_x + platform_width and  # Player's left edge < platform's right edge
                    sprite_sheet_image['y'] + 48 > platform_y and  # Player's bottom edge > platform's top edge
                    sprite_sheet_image['y'] + 48 <= platform_y + y_velocity  # Player is falling onto the platform
                    
                ):
                    sprite_sheet_image['y'] = platform_y - 48  # Place the player on top of the platform
                    y_velocity = 0 

            #gravity logic
            if sprite_sheet_image['y'] > 390:
                sprite_sheet_image['y'] = 390
                y_velocity = 0
            
            screen.blit(frame_0, (sprite_sheet_image['x'], sprite_sheet_image['y']))
            

            # Render all platforms
            for platform in platforms:
                pygame.draw.rect(
                    screen, BLACK, 
                    (platform["x"], platform["y"], platform["width"], platform["height"])
                )


            #screen.blit(frame_0, (0, 0))
            #screen.blit(frame_1, (75, 0))
            #screen.blit(frame_2, (150, 0))
            #screen.blit(frame_3, (225, 0))
            #screen.blit(frame_4, (300, 0))
            #screen.blit(frame_5, (375, 0))

            # keys things
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                sprite_sheet_image['x'] -= 5
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                sprite_sheet_image['x'] += 5
            if key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]:
                if sprite_sheet_image['y'] == 390 or any(
                    sprite_sheet_image['y'] == platform['y'] - 48 for platform in platforms
                ):
                    y_velocity = jump_strength
                #if sprite_sheet_image['x']! == platform['x']:
                    #y_velocity = jump_strength!

            # Prevent the player from moving off the screen
            if sprite_sheet_image["x"] < 0:
                sprite_sheet_image["x"] = 0
            if sprite_sheet_image["x"] + 48 > SCREEN_WIDTH:  # Assuming the player's width is 32
                sprite_sheet_image["x"] = SCREEN_WIDTH - 48
            if sprite_sheet_image["y"] < 0:
                sprite_sheet_image["y"] = 0
            if sprite_sheet_image["y"] + 48 > SCREEN_HEIGHT:  # Assuming the player's height is 32
                sprite_sheet_image["y"] = SCREEN_HEIGHT - 48

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

main()

pygame.quit()
sys.exit()
