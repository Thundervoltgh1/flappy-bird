import pygame,sys
pygame.init()
sw=800
sh=600
score=0
flying=False
screen= pygame.display.set_mode((sw,sh))
pygame.display.set_caption("FLAPPY BIRD")
screen.fill("white")
bg=pygame.image.load('fbg.png')
ground=pygame.image.load('fbground.png')

game_over=False
fps=50
font=pygame.font.SysFont('Bauhaus 93',60)

flying=False
pygame.display.update()

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.counter=0
        self.index=0
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        if game_over==False:
            self.counter+=1
            self.index+=1
            if self.index>=len(self.images):
                self.index=0
            self.image=self.images[self.index]

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
    screen.blit(ground,(ground_scroll,550))
    draw_text(str(score),10,10)
    ground_scroll-=ground_speed
    if abs(ground_scroll)>35:
        ground_scroll=0


    birdgroup.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
