import golds
import bricks
import bloods

def init(blood,reply,brick,gold,questionBox):
    setblood(blood)
    setreply(reply,questionBox)
    setbrick(brick)
    setgold(gold)

def setblood(blood):
    for i in range(3): #三顆血量
        blood.append(bloods.bloods())
        blood[i].position = [10 + 30 * i,10] #位置

def setreply(reply,questionBox):
    reply.show = False #隱藏
    reply.position = [questionBox.position[0],questionBox.position[1] - 30]
    
def setbrick(brick):
    for i in range(24): #24塊地板
        brick.append(bricks.bricks())
        brick[i].position = [brick[i].img.get_size()[0] * i,305]
        
def setgold(gold):
    for i in range(10): #10個金幣
        gold.append(golds.golds())
        if i < 5: #前5個金幣位置
            if i == 2:
                gold[i].position = [200 + 50 * i,160]
            else:
                gold[i].position = [200 + 50 * i,250]
        else: #後5個金幣位置
            if i == 7:
                gold[i].position = [500 + 50 * i,160]
            else:
                gold[i].position = [500 + 50 * i,250]
                