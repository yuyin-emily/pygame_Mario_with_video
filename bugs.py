import pygame

class bugs():
    def __init__(self):
        self.position = [700,240]
        self.img = [
            pygame.image.load("./image/bugr.png"),
            pygame.image.load("./image/bugl.png")
            ]
        self.show = True
        self.range = [self.position[0] - 100,self.position[0] + 100] #敵人移動範圍
        self.dirX = "right"
        self.speed = 3
    
    #小怪移動
    def run(self,chara): #左轉
            if self.position[0] > self.range[1]:
                self.dirX = "left"
                self.speed = 3
            elif self.position[0] < self.range[0]: #右轉
                self.dirX = "right"
                self.speed = 3
            
            #向玩家突刺         
            if self.dirX == "right":
                if chara.position[0] - self.position[0] < 200 and chara.position[0] - self.position[0] > 0:
                    self.speed = 6
                self.position[0] += self.speed
            else:
                if self.position[0] - chara.position[0] < 200 and self.position[0] - chara.position[0] > 0:
                    self.speed = 6
                self.position[0] -= self.speed
    
    #與小怪碰撞
    def touch(self,chara,questionBox):
        if abs(self.position[0] - chara.position[0]) < 40 and abs(self.position[1] - chara.position[1]) < 40: #計算是否重疊
            chara.life = False
            chara.blood -= 1
            questionBox.reset()
            self.position = [700,240]
            self.range = [self.position[0] - 100,self.position[0] + 100]
            self.dirX = "right"
            died_sound = pygame.mixer.Sound("./music/died.wav")
            died_sound.set_volume(0.5)
            died_sound.play()
            return True #返回,與小怪碰撞
        else:
            return False #返回,無事發生
    
    def reset(self):
        self.position = [700,240]
        self.show = True
        self.dirX = "right"
        self.speed = 3
        
    def istouch(self,chara):
        selfCenter = [self.position[0] + self.img[0].get_width(),self.position[0] + self.img[0].get_width()]