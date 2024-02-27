import pygame

class questionBoxs():
    def __init__(self):
        self.position = [355,140]
        self.img = [pygame.image.load("./image/qq.png"),pygame.image.load("./image/qqafter.png")]
        self.show = False
        self.touch = False
        
    def touching(self,chara,reply):
        if abs(chara.position[0] - self.position[0]) < self.img[0].get_size()[0] // 2 :
            if chara.position[1] <= 140+self.img[0].get_size()[1]:
                chara.diry = "down"
                if self.touch == False:
                    reply.show = True
                    if chara.blood < 3:
                        chara.blood += 1
                self.touch = True
                
        
    def run(self):
        self.position[0] -= 10
        
    def reset(self):
        self.position = [355,140]
        self.show = False
        self.touch = False
