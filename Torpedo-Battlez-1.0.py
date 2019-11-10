import pygame
import math
import random
from pygame import mixer
mixer.init()
import time
strike_cnt = 0
score = 0
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Torpedo Battlez | Update 1.0")
file = pygame.image.load('ShipBattleshipHull.png')
miss = pygame.image.load('spr_missile.png')
other = pygame.image.load('Missile.png')
destroyerimg = pygame.image.load('ShipDestroyerHull.png')
destroyerflipimg = pygame.image.load('destcop.png')
direc = 0
planeimg = pygame.image.load('PlaneF-35Lightning2.png')
def iscol(player1x, player2x, player1y, player2y):
    distance_eq = math.sqrt((math.pow(player1x - player2x, 2)) + (math.pow(player1y - player2y, 2)))
    if distance_eq < 75:
        return True
    else:
        return False
airvel = 10

class ship():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class missile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class destroyer():
    def __init__(self,x,y,ycount,xcount,vel,velcount,bool):
        self.x = x
        self.y = y
        self.ycount = ycount
        self.xcount = xcount
        self.vel=vel
        self.velcount=velcount
        self.bool = bool
    def draw(self):
        win.blit(destroyerimg, (self.x, self.y))
    def movement(self):
        global direc
        if self.ycount==0:
            self.y += self.vel
            direc=0
        if self.y >= 550:
            self.ycount=1
        if self.ycount==1:
            self.y-=self.vel
            direc=1
        if self.y<=-125:
            self.ycount=0
        if self.velcount<10:
            self.vel=10
            self.velcount+=1
        if self.velcount > 10:
            self.vel=15
            self.velcount+=1
        if self.velcount > 20:
            self.vel=10
            self.velcount=0
class aircraft():
    def __init__(self, x, y, fly):
        self.x = x
        self.y = y
        self.fly = fly
    def draw(self):
        win.blit(planeimg, (destroyer1.x,self.y))
    def movement(self):
        win.blit(planeimg, (destroyer1.x,self.y))
        self.y-=15
        if iscol(destroyer1.x,self.x, destroyer1.y, self.y):
            self.fly = False
            print("collidied with dest")
            pygame.mixer.music.load('explosion2.mp3')
            pygame.mixer.music.play(0)
            destroyer1.bool = True
            destroyer1.y = 600
destroyer1 = destroyer(400, 200, 0, 0, 8,0,True)
destroyer2 = destroyer(450, 750, 0, 0, 8,0,True)
aircraft1=aircraft(destroyer1.x,700,False)

battleship = ship(40, 50)
bulletstate = "ready"
bulx = battleship.x+10
buly=battleship.y+50
bulx2 = battleship.x+10
buly2=battleship.y+120
def draw():
    win.blit(other, (bulx , buly))
    win.blit(other, (bulx2, buly2))

runup = False
rundown = False
run = True
velocity = 5
t_vel = 2
yes = True
playmus = True
while run:
    if playmus == True:
        pygame.mixer.music.load('IgnoranceIsBliss.mp3')
        pygame.mixer.music.play(-1)
        playmus = False
    pygame.time.delay(50)
    win.fill((43, 131, 219))
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_UP] and battleship.y > 0:
        battleship.y -= velocity
        runup = True
    if keypress[pygame.K_DOWN] and battleship.y < 450:
        battleship.y += velocity
        rundown = True
    if keypress[pygame.K_RIGHT] and battleship.x < 80:
        battleship.x += t_vel
    if keypress[pygame.K_LEFT] and battleship.x > 0:
        battleship.x -= t_vel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                battleship.x -= random.randint(1,2)
                if bulletstate == "ready":
                    print("Fire!")
                    draw()
                    bulletstate = "fired"
                    pygame.mixer.music.load('Launch.wav')
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_a and strike_cnt<=1:
                strike_cnt=300
                print("hi")
                aircraft1.fly = True
                aircraft1.y=550
    if bulletstate == "fired":
        bulx += 10
        bulx2 += 10
        draw()
    if bulletstate == "ready":
        bulx = battleship.x + 10
        buly = battleship.y + 50
        bulx2 = battleship.x + 10
        buly2 = battleship.y + 150
    if bulx >= 500:
        bulletstate = "ready"
    if iscol(bulx,destroyer1.x,buly,destroyer1.y):
        pygame.mixer.music.load('explosion2.mp3')
        pygame.mixer.music.play(0)
        score += 10
        destroyer1.bool=True
        destroyer1.y = 800

    miss.blit(miss, (430,200))
    win.blit(file, (battleship.x,battleship.y))
    if destroyer1.bool == True:
        if direc==1:
            win.blit(destroyerimg, (destroyer1.x, destroyer1.y))
            destroyer1.movement()
        if direc==0:
            win.blit(destroyerflipimg, (destroyer1.x, destroyer1.y))
            destroyer1.movement()
    if aircraft1.fly == True:
        aircraft1.movement()
    if strike_cnt > 0:
        strike_cnt -= 1
    renderthis2 = pygame.font.SysFont('freesansbold.tff', 25).render("Score: " + str(score),1,(0, 255, 0))
    win.blit(renderthis2, (400, 15))
    controls = pygame.font.SysFont('freesansbold.tff', 25).render("SPACE - Fire / A - Airstrike",1,(0, 255, 0))
    # win.blit(planeimg, (50,50))
    win.blit(controls, (5, 15))
    pygame.display.update()
pygame.quit()
