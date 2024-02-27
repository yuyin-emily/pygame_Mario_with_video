import pygame
import sys

import charas
import questionBoxs
import golds
import bricks
import bugs
import bloods
import image
import music

import init
import drawAndWrite

def main():
    #製造中,loading...
    chara = charas.charas() #角色
    bug = bugs.bugs() #敵人
    gold = [] #金幣
    brick = [] #地板
    blood = [] #血量
    reply = bloods.bloods() #回血道具
    questionBox = questionBoxs.questionBoxs() #問號箱
    
    
    init.init(blood,reply,brick,gold,questionBox)
    
    #遊戲初始化
    pygame.init()
    pygame.display.set_caption("The Great Adventure!")
    screen = pygame.display.set_mode((640,360)) #遊戲視窗
    clock = pygame.time.Clock()

    #匯入背景音樂並播放
    pygame.mixer.music.load("./music/bg_music.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    min_score = 500 #最高紀錄（最短耗時）
    num = 0 #獲得金幣數量
    run = True #遊戲迴圈
    play = True #遊玩狀態
    level = 1 #關卡
    
    #遊戲迴圈
    while run:
        while play:
            if not pygame.mixer.music.get_busy(): #bgm循環
                pygame.mixer.music.play()
            
            num += 1
            #關閉視窗及調整視窗大小
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #遊戲強制結束
                    play = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1: #全螢幕
                        screen = pygame.display.set_mode((640,360),pygame.FULLSCREEN)
                    if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE: #視窗
                        screen=pygame.display.set_mode((640,360))
            
            #血量歸0
            if chara.blood == 0:
                play = False
                break
            
            #抓鍵盤
            if chara.position[1] <= 210:
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_TAB]:
                    chara.blood = 0
                    play = False
                    pygame.time.wait(200)
                    break
        
                if chara.position[0] > 400: #偵測是否走到底
                    if keys[pygame.K_RIGHT]: #偵測是否換關
                        if brick[23].position[0] >= 640 - brick[23].img.get_size()[0]: #背景移動
                            for i in range(24):
                                brick[i].run()
                            if level == 3: #設置敵人
                                bug.range[0] -= 10
                                bug.range[1] -= 10
                                questionBox.run()
                            if level == 1: #設置金幣
                                for i in range(10):
                                    gold[i].run()
                        else:
                            if chara.position[0] == 550: #初始化背景
                            #根據各關情況初始化背景
                                if level == 2: #第二關
                                    brick[5].show = True #地板顯示
                                    brick[10].show = True #地板顯示
                                    brick[15].show = True #地板顯示
                                    level = 3 #進入第三關
                                    questionBox.show = True
                                    chara.reset()
                                    for i in range(24):
                                        brick[i].position = [brick[i].img.get_size()[0] * i,305]
                                    pygame.time.wait(500)   
                                elif level == 1: #第一關
                                    goldQuantity = 0 #初始化金幣數量
                                    for i in range(10): #所有金幣
                                        if gold[i].show: #顯示金幣
                                            gold[i].eat(chara.position) #吃到金幣的行動
                                            screen.blit(gold[i].img[(num % 80) // 40],gold[i].position) #左右變換
                                            goldQuantity += 1
                                    if goldQuantity == 0: #收集所有金幣後
                                        level = 2 #進入第二關
                                        chara.reset()
                                        for i in range(24):
                                            brick[i].position = [brick[i].img.get_size()[0] * i,305]
                                        pygame.time.wait(500)
                                elif level == 3: #第三關
                                        play = False #結束遊戲
                                        if int(num // 10) < int(min_score):
                                            min_score = int(num // 10) 
                                        #pygame.wait(1000)
                            else:
                                chara.run(keys) #當前關卡未結束
                    else:
                        chara.run(keys) #如果角色未向右移動
                            
                else:    
                    chara.run(keys) #如果角色沒有走到底
                
                #偵測是否掉落
                for i in range(24):
                    if brick[i].drop(chara,chara.position):
                        for i in range(24):
                            brick[i].position = [brick[i].img.get_size()[0] * i,305]
                        break
                    
            drawAndWrite.drawIcon(brick,blood,questionBox,reply,screen,chara,bug,num)
                    
            #掉落
            chara.down()
            
            #彈跳
            chara.jumping()
            
            #初始化回血教具
            reply.show = False
            reply.position = [questionBox.position[0],questionBox.position[1] - 30]
            
            if questionBox.show:
                questionBox.touching(chara, reply)
            
            
            #各關背景設定
            if level == 2: #第二關
                brick[5].show = False #隱藏地板
                brick[10].show = False #隱藏地板
                brick[15].show = False #隱藏地板
            elif level == 1: #第一關
                for i in range(10):
                    if gold[i].show:
                        gold[i].eat(chara.position)
                        screen.blit(gold[i].img[(num % 80) // 40], gold[i].position)
            elif level == 3: #第三關
                bug.run(chara)
                questionBox.show = True
                if bug.touch(chara,questionBox):
                    chara.reset()
                    for i in range(24):
                        brick[i].position = [brick[i].img.get_size()[0] * i, 305]
                
            pygame.display.update()
            clock.tick(55) #參數越大刷新越快
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #遊戲結束
        drawAndWrite.writeText(chara,screen,num,min_score)
            
        keys = pygame.key.get_pressed()
        
        #遊戲重啟
        if keys[pygame.K_TAB]:
            play = True
            num = 0
            level = 1
            bug.reset()
            chara.reset()
            chara.blood = 3
            questionBox.reset()
            for i in range(24):
                brick[i].reset(i)
            for i in range(10):
                gold[i].setPosition(i)
            pygame.time.wait(200)

        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()