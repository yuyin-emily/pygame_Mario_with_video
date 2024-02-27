import pygame

class bricks():
    def __init__(self):
        self.position = [355,150] #位置
        self.img = pygame.image.load("./image/bl.png")
        self.show = True #顯示
    
    #角色失足
    def drop(self,chara,chara_position):
        if not self.show and chara_position[1] >= 210 and chara_position[0] > self.position[0] and chara_position[0] < self.position[0] + self.img.get_size()[0] // 4: #條件1:blocks.show = True, 條件2:chara[y] >= 210, 條件3:chara[x]位於範圍內
            chara.life = False #角色死亡
            chara.blood -= 1 #血量 - 1
            diedSound = pygame.mixer.Sound("./music/died.wav")
            diedSound.set_volume(0.5)
            diedSound.play()
            return True #返回,碰撞發生
        else:
            return False #返回,無事發生
            
    def run(self):
        self.position[0] -= 10
        
    def reset(self,i):
        self.show = True
        self.position = [self.img.get_size()[0] * i,305]