import pygame
import image

def drawIcon(brick,blood,questionBox,reply,screen,chara,bug,num):
    drawBackground(screen)
    drawBrick(brick,screen)
    drawBlood(blood,screen,chara)
    drawquestionBox(questionBox,screen)
    drawReply(reply,screen)
    drawBug(bug,screen)
    drawLevel(brick,screen)
    drawChara(chara,screen,num)
    
def writeText(chara,screen,num,min_score):
    font = pygame.font.Font(None, 80)
    if chara.blood == 0:
        failText(font,screen)
    else:
       successText(font,screen,num,min_score)
    

def drawBackground(screen):
    img_bg = pygame.image.load("./image/pg_bg.png")
    for i in range(5):
        screen.blit(img_bg,[i * 160,0])

def drawBrick(brick,screen):
    for i in range(24):
        if brick[i].show:
            screen.blit(brick[i].img,brick[i].position)
                    
def drawBlood(blood,screen,chara):
    for i in range(chara.blood):
        if blood[i].show:
            screen.blit(blood[i].img,blood[i].position)
                    
def drawquestionBox(questionBox,screen):
    if questionBox.show:
        if questionBox.touch:
            screen.blit(questionBox.img[1],questionBox.position)
        else:
            screen.blit(questionBox.img[0],questionBox.position)
                    
def drawReply(reply,screen):
    if reply.show:
        screen.blit(reply.img,reply.position)
        
def drawBug(bug,screen):
    if bug.dirX == "right":
        screen.blit(bug.img[0],bug.position) 
    else:
        screen.blit(bug.img[1],bug.position) 
        
def drawLevel(brick,screen):
    screen.blit(pygame.image.load("./image/level.png"),[brick[23].position[0],brick[23].position[1] - 50])
    
def drawGold(gold,screen,num):
    for i in range(10):
        screen.blit(gold[i].img[(num % 80) // 40],gold[i].position)

def drawChara(chara,screen,num):
    if chara.dirX == "right":
        screen.blit(chara.img[(num % 80) // 40],chara.position)
    else:
        screen.blit(chara.img[(num % 80) // 40 + 2],chara.position)  
        
                
def successText(font,screen,num,min_score):
    text_surface1 = font.render("WIN! Time:" + str(num//10),True,(0,0,255)) #本次遊戲分數
    text_surface2 = font.render("Hightest:" + str(min_score),True,(0,0,255)) #歷史最高
    
    #位置
    text_rect1 = text_surface1.get_rect()
    text_rect2 = text_surface2.get_rect()
    text_rect1.center = (screen.get_size()[0] // 2,screen.get_size()[1] // 2 - 50)
    text_rect2.center = (screen.get_size()[0] // 2,screen.get_size()[1] // 2 + 50)
    screen.blit(text_surface1,text_rect1)
    screen.blit(text_surface2,text_rect2)


def failText(font,screen):
    text_surface1 = font.render("Game over!",True,(0,0,255))
    text_rect1 = text_surface1.get_rect()
    text_rect1.center = (screen.get_size()[0] // 2,screen.get_size()[1] // 2)
    screen.blit(text_surface1,text_rect1)