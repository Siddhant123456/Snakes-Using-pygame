import pygame
import random
import os
pygame.mixer.init()
pygame.init()

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My First Game')

bgimg = pygame.image.load("background.jpg")
bgimg = pygame.transform.scale(bgimg , (screen_width,screen_height)).convert_alpha()

pygame.image.load(os.path.join('background.jpg'))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def show_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
    

def print_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((250,200,200))
        print_score("Welcome To Snakes" , (0,0,0) , 130,250)
        print_score("Press Spacebar To Play" , (0,0,0) , 110,280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        clock.tick(60)
        pygame.display.update()
        


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 60
    snake_size = 20
    red = (255,0,0)
    white = (255,255,255)
    black = (0,0,0)
    fps = 30
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    snk_list = []
    snk_length = 1
     
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt" , "w") as f:
            f.write("0")
    else:
        with open("highscore.txt" , "r") as f:
            highscore = f.read()
  
            
    while not exit_game:
        if game_over:
            
            gameWindow.fill(black)
            
            
            with open("highscore.txt" , "w") as f:
                f.write(str(highscore))
            print_score("Game Over Press Enter To Continue",red,130,250)
            

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
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = +10
                        velocity_x = 0
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                snk_length += 5
                food_x = random.randint(0,900)
                food_y = random.randint(0,600)
                if score > int(highscore):
                    highscore = score
            snake_x += velocity_x
            snake_y += velocity_y
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            
           
            
            gameWindow.fill(black)
            gameWindow.blit(bgimg,(0,0))
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
           
            print_score("Score:  " + str(score) + " High Score :"  + str(highscore), red,5,5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            

            show_snake(gameWindow,black,snk_list,snake_size)



    
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()

welcome()

