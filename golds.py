import pygame

class golds():
    def __init__(self):
        self.position = [355,250] #位置
        self.img = [pygame.image.load("./image/ggl.png"),
                  pygame.image.load("./image/ggr.png")
                  ] #匯入圖片(金幣左、金幣右)
        self.show = True #顯示
    
    #角色吃到金幣
    def eat(self,chara_position):
        if abs(chara_position[0] - self.position[0]) < 20 and abs(chara_position[1] - self.position[1]) < 50: #計算角色是否與金幣重疊
            self.show = False #隱藏
            goldSound = pygame.mixer.Sound("./music/gg.wav") #金幣音效
            goldSound.set_volume(0.5) #音量
            goldSound.play() #播放
            
    def run(self): #左移(配合地圖)
        self.position[0] -= 10
        
    def setPosition(self,i):
        self.show = True
        if i < 5:
            if i == 2:
               self.position = [200 + 50 * i, 160]
            else:
                self.position = [200 + 50 * i, 250]
        else:
            if i == 7:
                self.position = [500 + 50 * i, 160]
            else:
                self.position = [500 + 50 * i, 250]