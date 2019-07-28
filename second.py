import pygame



pygame.init()


screen_width = 800
screen_height =  500

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bounce")


black = (0,0,0)
# Game Loop
exit_game = False
x = 200
y = 285
size1 = 50
size2 = 90
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        
    gameWindow.fill((255,255,255))
    pygame.draw.line(gameWindow,black,(0,3*(screen_height)/4),(screen_width,3*(screen_height)/4))
    while x<screen_width:
        pygame.draw.rect(gameWindow,black,[x,y,size1,size2])
        x = x + 100
        pygame.display.update()
    
    
    
        

