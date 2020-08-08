
import pygame
import time
import random
from random import sample

pygame.init()


base_font = pygame.font.Font(None , 48)


smallfont = pygame.font.SysFont("comicsansms", 25)

rect = pygame.Rect(145, 200, 80, 80)
clock = pygame.time.Clock()

limits = [10, 30, 50, 70, 90, 120, 150, 180, 200, 220]


white = (255, 255, 255)
blue = (0, 0, 128) 
red = (255,0,0)
yellow  = (255, 255, 0)
black = (0,0,0)
light_red = (255,0,0)
green = (134, 68, 235)
light_green = (164, 117, 235)
sapgreen = (212, 230, 57)

display_width = 400
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
display_surface = pygame.display.set_mode((display_width,display_height)) 
screen = gameDisplay

pygame.display.set_caption('The_Card_Game')

X = 400




red = (200,0,0)
light_red = (255,0,0)




def clear_screen():
    display_surface.fill((0,0,0))

def delay():
    pygame.time.wait(4000)

def randnumbers(count):
    return(sample(range(limits[count]),8))

def which_number():
    index = sample((0,7) ,1)
    return(index[0]+1)


def original():
    pygame.draw.rect(display_surface , (255,255,0) ,(17,85,80,135))
    pygame.draw.rect(display_surface , (127 , 123,0) , (113 , 85 , 80 , 135))
    pygame.draw.rect(display_surface,(124,0,255),(208,85,80,135))
    pygame.draw.rect(display_surface , (255,0,255) , (300 , 85 , 80 , 135))
    pygame.draw.rect(display_surface , (255,123,89) ,(17,240,80,135))
    pygame.draw.rect(display_surface , (45,123,89) ,(113,240,80,135))
    pygame.draw.rect(display_surface , (45,243,89) ,(113,240,80,135))
    pygame.draw.rect(display_surface , (187,123,7) ,(208,240,80,135))
    pygame.draw.rect(display_surface , (45,13,89) ,(300,240,80,135))
        

def flip(count):
    
    pygame.draw.rect(display_surface , (255,255,255) ,(17,85,80,135))
    pygame.draw.rect(display_surface , (255 , 255,255) , (113 , 85 , 80 , 135))
    pygame.draw.rect(display_surface,(255,255,255),(208,85,80,135))
    pygame.draw.rect(display_surface , (255,255,255) , (300 , 85 , 80 , 135))
    pygame.draw.rect(display_surface , (255,255,255) ,(17,240,80,135))
    pygame.draw.rect(display_surface , (255,255,89) ,(113,240,80,135))
    pygame.draw.rect(display_surface , (255,255,255) ,(113,240,80,135))
    pygame.draw.rect(display_surface , (255,255,255) ,(208,240,80,135))
    pygame.draw.rect(display_surface , (255,255,255) ,(300,240,80,135))
    
    cX = [55,151,246,338,55,151,246,338]
    cY = [154,154,154,154,308,308,308,308]

    arr = randnumbers(count)
    values = arr
   
    for i, j in enumerate(arr):
        text , textRect = numberpos(j)
        textRect.center = (cX[i], cY[i])
        display_surface.blit(text , textRect)
    return(values)


def numberpos(num):
    font = pygame.font.Font('freesansbold.ttf', 36)
    text = font.render(str(num), True,(0,0,0) , (255,255,255))
    textRect = text.get_rect()
    return(text , textRect)


def level(count):
        font = pygame.font.Font('freesansbold.ttf', 28) 
        text = font.render('STAGE ' + str(count+1) , True, white, (0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (X // 2, 20)
        display_surface.blit(text , textRect)

  
def intro():
       
        font = pygame.font.Font('freesansbold.ttf', 24) 
        text = font.render('THE ULTIMATE MEMORY TEST' , True, white, (0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (200,100)
        display_surface.blit(text , textRect)
        font = pygame.font.Font('freesansbold.ttf', 72) 
        text = font.render('cOuNt ThE' , True, white, (0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (196,200 )
        display_surface.blit(text , textRect)
        font = pygame.font.Font('freesansbold.ttf', 72) 
        text = font.render('CASES' , True, white, (0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (240, 320)
        display_surface.blit(text , textRect)
        pygame.display.update()
        pygame.time.wait(4000)

def rules():
    pass

def game(count):
     
        display_surface.fill((0,0,0))
        Win = True
        while Win:
            clear_screen()
            level(count)
            original()
            pygame.display.update()
            values = flip(count)
            delay()
            pygame.display.update()
            delay()
            original()
            pygame.display.update()
            delay()
            clear_screen()
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    quit() 
            Win = False
            break
        return(values , count)

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)


def button(count , text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "play":
                d(count)
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)
        


def game_intro(count):

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:
                        
                        pygame.quit()
                        quit()

        gameDisplay.fill((204, 238, 255))
        font = pygame.font.Font('freesansbold.ttf', 34) 
        text = font.render('Hard Luck :(' , False,(0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (200,100)
        display_surface.blit(text , textRect)
       

        button(count , "Play Again", 50,200,140,80, green, light_green, action="play")
     
        button(count ,"Quit", 240,200,100,80, red, light_red, action ="quit")



        pygame.display.update()

        clock.tick(15)


def d(count):
    running = True
    user = ''
    values , count = game(count)
    index = random.randint(1, 8)
    while running:
        screen.fill(yellow)
     

        text = smallfont.render('Cases in country ' + str(index) + ' ?' , False, (0,0,0)) 
        textRect = text.get_rect() 
        textRect.center = (200,100)
        screen.blit(text , textRect)
      
      
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user = user[:-1]
            if event.key == pygame.K_RETURN:
                if len(user) > 0:
                    running = False
            else:
                user += event.unicode
                
        pygame.draw.rect(screen , black , rect , 2)
        text_surface = base_font.render(user , True ,(0,0,0))
        screen.blit(text_surface,(rect.x + 20 , rect.y + 30))
        pygame.display.update()
       

    check(count , int(user) , values[index-1])

def text(msg , center , size):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(msg , False, (0,0,0)) 
    textRect = text.get_rect() 
    textRect.center = center
    screen.blit(text , textRect)

def check(count , user , on_card_val):
    if user == on_card_val:
        screen.fill((255,255,9))
        font =  pygame.font.SysFont("comicsansms", 36)
        text = font.render('CONGRATULATIONS',False, (0,0,0)) 
        pygame.time.delay(1000)
        textRect = text.get_rect() 
        textRect.center = (200,100)
        screen.blit(text , textRect)
        font =  pygame.font.SysFont("comicsansms", 28)
        text = font.render('Get Ready for the next round',False, (0,0,0)) 
        pygame.time.delay(1000)
        textRect = text.get_rect() 
        textRect.center = (200,200)
        screen.blit(text , textRect)
        pygame.display.update()
        count += 1
        pygame.time.delay(3000)
        d(count)
    
    else:
        game_intro(count)
        
def call(count):
    intro()
    d(count)


if __name__ == "__main__":
    
     count = 0
     call(count)



