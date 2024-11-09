import pygame,sys
import random
pygame.init()
sw=800
sh=600
score=0
speed=5
flying=False
screen= pygame.display.set_mode((sw,sh))
pygame.display.set_caption("FLAPPY BIRD")
screen.fill("white")
bg=pygame.image.load('fbg.png')
ground=pygame.image.load('fbground.png')
pipe_freq=1500
pipe_gap=150
passpipe=False

game_over=False
fps=50
font=pygame.font.SysFont('Bauhaus 93',60)
lastpipe= pygame.time.get_ticks()-pipe_freq
flying=False
pygame.display.update()

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipe.png")
        self.rect=self.image.get_rect()
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-(pipe_gap/2)]
        elif position==-1:
            self.rect.topleft=[x,y+(pipe_gap/2)]
    def update(self):
        self.rect.x-=speed
        
pipegroup=pygame.sprite.Group()

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.counter=0
        self.index=0 
        self.vel=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.clicked=False
    def update(self):
        
        if game_over==False:
            self.counter+=1
            self.index+=1
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        
            if self.index>=len(self.images):
                self.index=0
            self.image=self.images[self.index]
    
        if flying== True:
            self.vel+=0.5
            if self.vel>8:
                self.vel=8
            if self.rect.bottom<550:   
                self.rect.y+=self.vel


flappy=Bird(100,sh/2)
birdgroup=pygame.sprite.Group()
birdgroup.add(flappy)
clock=pygame.time.Clock()
ground_speed=4
ground_scroll=0
def draw_text(txt,x,y):
    img=font.render(txt,True,'white')
    screen.blit(img,(x,y))

while True:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    pipegroup.draw(screen)
    screen.blit(ground,(ground_scroll,550))
    
    ground_scroll-=ground_speed
    if abs(ground_scroll)>35:
        ground_scroll=0
    if len(pipegroup)>0:
        if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.left\
        and birdgroup.sprites()[0].rect.right<pipegroup.sprites()[0].rect.right and passpipe==False:
            passpipe=True
        if passpipe==True:
            if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.right:
                score+=1
                print(score)
                print(passpipe)
                passpipe=False
    
    draw_text(str(score),10,10)

    if flying==True and game_over==False:
        time_now=pygame.time.get_ticks()
        if time_now-lastpipe>pipe_freq:
            pheight=random.randint(-100,100)

            bpipe=Pipe(sw,sh//2+pheight,-1)
            pipegroup.add(bpipe)
            tpipe=Pipe(sw,sh//2+pheight,1)
            pipegroup.add(tpipe)
            lastpipe=time_now
            
    birdgroup.update()
    pipegroup.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
 
    pygame.display.update()
