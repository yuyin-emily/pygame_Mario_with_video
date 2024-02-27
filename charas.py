import pygame

class charas():
    def __init__(self):
        self.position = [50,210]
        self.img = [
                    pygame.image.load("./image/01.png"),
                    pygame.image.load("./image/02.png"),
                    pygame.image.load("./image/03.png"),
                    pygame.image.load("./image/04.png")
                ]
        self.speed = 10 #移速
        self.dirX = "right" #方向右
        self.dirY = "None" #跳躍(初始為否)
        self.life = True #存活狀態
        self.blood = 3 #血量
    
    def run(self,keys):
        jump_sound = pygame.mixer.Sound("./music/jump.wav")
        
        #角色移動
        if keys[pygame.K_UP]:
            if self.dirY =="None":
                self.dirY = "up"
                jump_sound.set_volume(0.5)
                jump_sound.play()
        if keys[pygame.K_LEFT] and self.life:
            if self.position[0] > 10:
                self.position[0] -= self.speed
                self.dirX = "left"
        if keys[pygame.K_RIGHT] and self.life:
            if self.position[0] <= 550:
                self.position[0] += self.speed
                self.dirX = "right"
    
    #跳躍
    def jumping(self):
        #視高度調整速度
        if self.position[1] < 140:
            self.dirY = "down"
        if self.dirY == "down":
            if self.position[1] >= 210:
                self.dirY = "None"
        if self.dirY == "up":
            self.position[1] -= self.speed * (1 + self.position[1] // 1000)
        elif self.dirY == "down":
            self.position[1] += self.speed * (1 + self.position[1] // 1000)
    
    #角色死亡動畫
    def down(self):
        if not self.life:
            self.jump = False
            if self.position[1] < 460: #角色尚未落地
                self.position[1] += self.speed #增加下墜速度
            else:
                self.reset() #重置

    #角色重置
    def reset(self):
        self.position = [50,210] #返回起始位置
        self.dirX = "right"
        self.jump = False
        self.jump_s = 0
        self.life = True