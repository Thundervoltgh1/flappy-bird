import pygame,sys
pygame.init()
sw=800
sh=850
screen= pygame.display.set_mode((800,850))
pygame.display.set_caption("FLAPPY BIRD")
screen.fill("white")
bg=pygame.image.load('fbg.png')
game_over=False
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
while True:
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
