import pygame
import random
import math as m
pygame.init()
screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("alien invasion")
icon=pygame.image.load("alien-head.png")
pygame.display.set_icon(icon)

backgroun_img=pygame.image.load("backgroung.jpg")
b_x=500
b_y=600


space_shipimg=pygame.image.load("arcade-game.png")
p_x=250
p_y=550
p_x_change=0

enemy_img=[]
e_x=[]
e_y=[]
e_x_change=[]
e_y_change=[]
num_of_enemies=7
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("alien.png"))
    e_x.append(random.randint(0,400 ))
    e_y.append(random.randint(0,0))
    e_x_change.append(0.1)
    e_y_change.append(40)
#you cant see the bullet

bullet_img=pygame.image.load("bullet.png")
bu_x=0
bu_y=550
bu_x_change=0
bu_y_change= 0.4
bu_state="ready"

#score count
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

game_over_font=pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    final_text=game_over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(final_text,(200,250))
def show_score(x,y):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(space_shipimg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bu_state
    bu_state="fire"
    screen.blit(bullet_img,(x+6,y+5))
#here y see did bullet fire from the tip of the nose
# and x see whether the bullet appear at the centre of the image
    #bu_x=x
    #bu_y=y   
def collidee(e_x,e_y,bu_x,bu_y): 
    dist=m.sqrt(m.pow(e_x-bu_x,2)+m.pow(e_y-bu_y,2))
    if dist<27:
        return True
    else:
        return False
     
running=True
while running:
    screen.fill((255,0,0))
    screen.blit(backgroun_img,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_x_change=-0.1
            if event.key == pygame.K_RIGHT:
                 p_x_change = 0.1
            if event.key == pygame.K_SPACE:
                if bu_state is "ready": #it check whether it is in screen or not
                    bu_x=p_x
                    fire_bullet(bu_x,bu_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                   p_x_change = 0
    #checking boundery for rocket
    p_x += p_x_change
    
    if p_x<=0:
        p_x = 0
    elif p_x>=460:
        p_x=460
    # enemy checking boundery  
    #here we have create multiple enemy and have also check collision of each enemy  aganist the bullet
    for i in range(num_of_enemies):
         if e_y[i]>440: #gameoverlogic
            for j in range(num_of_enemies):
                e_y[j]=2000
                game_over_text()
                break
                
         e_x[i] += e_x_change[i]
         if e_x[i]<=0:
            e_x_change[i] = 0.1
            e_y[i] +=e_y_change[i]
         elif e_x[i]>=460:
            e_x_change[i]= -0.1
            e_y[i] +=e_y_change[i]
         collision = collidee(e_x[i],e_y[i],bu_x,bu_y)
         if collision:
           bu_y=520
           bu_state="ready"
           score_value+=1
           e_x[i]=random.randint(0,400)
           e_y[i]=random.randint(0,30)
         enemy(e_x[i],e_y[i],i) 
    #bullet
    if bu_y<=0:
        bu_y=520
        bu_state="ready"
    if bu_state is "fire":
        fire_bullet(bu_x,bu_y)
        bu_y -=bu_y_change 
 
    player(p_x,p_y)
    show_score(textX,textY)
  
    pygame.display.update()