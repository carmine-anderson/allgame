"""Snake Game :)"""

import pygame
import time
import random
import pygame.mixer

pygame.mixer.init()
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 172, 28)

jumpscare_display = False

dis_width = 700
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Haunted Snake Game by Carmine')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

background_image = pygame.image.load("halloween2.jpeg")
background_image2 = pygame.image.load("starter_backgroung.jpeg")
momo = pygame.image.load("momo.png")

eat_sound = pygame.mixer.Sound("eating_sound.mp3")
jumpscare_sound = pygame.mixer.Sound("jumpscare_sound.mp3")
bg_music = pygame.mixer.Sound("horror.mp3")
dc_join = pygame.mixer.Sound("discord.mp3")

# new_width = 10
# new_height = 8
# resized_ghost = ghost_image.resize((new_width, new_height))

dis.blit(background_image2, (0, 0))
pygame.display.update()

# Jumpscare
def display_jumpscare():
    dis.blit(momo, (0, 0))
    pygame.display.update()
    time.sleep(1)

def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        # if x == snake_list[0]:  # Draw the ghost image as the snake head
        #     dis.blit(ghost_image, (x[0], x[1]))
        # else:
        #     pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

        # dis.blit(ghost_image, (x[0], x[1]))
        # pygame.display.update()

        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():

    bg_music.play()

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0 
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10,0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        dis.blit(background_image2, (0, 0))
        pygame.display.update()

        while game_close == True:
            if Length_of_snake < 2:
                dis.blit(background_image, (0, 0))
                message("Don't play if you do not want to play..", white)
                pygame.display.update()
                time.sleep(3)
                game_over = True
                game_close = False

            elif jumpscare_display:
                jumpscare_sound.play()
                display_jumpscare()
                jumpscare_display = False
            dis.blit(background_image, (0, 0))
            message("You Lost! Press C-Play Again or Q-Quit", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            dc_join.play()
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, orange, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

    
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            jumpscare_display = True
            eat_sound.play()
        
        clock.tick(snake_speed)

    pygame.mixer.quit()
    pygame.quit()
    quit()


gameLoop()