import random
import easygui as g 


secret = random.randint(1,10)

i = 1
while(i!=4):
    temp = g.integerbox(msg="不妨猜一下小甲鱼现在心里想的是哪个数字（0-10）：",title="数字小游戏",lowerbound=0,upperbound=10)
    #temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    if guess == secret:
        #print("卧槽，你是小甲鱼心里的蛔虫吗？！\n哼，猜中了也没有奖励！")
        g.msgbox(msg="卧槽，你是小甲鱼心里的蛔虫吗？！\n哼，猜中了也没有奖励！",title="答案",ok_button="退出")
        #print("游戏结束，不玩啦^_^")
        break
    elif guess < secret:
        #print("猜错啦，比这个%d更大"%guess)
        g.msgbox(msg="猜错啦，比这个%d更大"%guess,title="答案",ok_button="继续")
        i=i+1
    else :
        #print("猜错啦，比这个%d更小"%guess)
        i=i+1
        g.msgbox(msg="猜错啦，比这个%dd更小"%guess,title="答案",ok_button="继续")

