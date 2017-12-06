'''
Created on 2017年12月4日

@author: 魏来
'''
#import os
import random
from davinciCode import card
from davinciCode import game

if __name__ == '__main__':
    preparedCardList = []
    i=0
    while i<=11:
        cardW=card.Card(i,'w','noOne')
        cardB=card.Card(i,'b','noOne')
        preparedCardList.append(cardW)
        preparedCardList.append(cardB)
        i+=1
    cardWW=card.Card(-1,'w','noOne',0)
    cardBW=card.Card(-1,'b','noOne',0)
    preparedCardList.append(cardWW)
    preparedCardList.append(cardBW)
    random.shuffle(preparedCardList)
    
    myCardList=[]
    hisOrHerCardList=[]
    game.prepareCards(preparedCardList, myCardList, hisOrHerCardList)
    for card in hisOrHerCardList:
        if(card.number==-1):
            randNum=random.randint(0,11)
            card.setRegards(randNum)
    
    game.printAllCards(hisOrHerCardList)
    game.printAllCards(myCardList)
    userGotHyphen=False
    for card in myCardList:
        if(card.number==-1):
            userGotHyphen=True
            print('你抽到了'+('黑' if card.color=='b' else '白')+'色的横杠，你要把它当做什么数字用？')
            needInput=True
            while needInput:
                num=input("请输入0~11的数字，或输入h进入帮助菜单，或输入q退出游戏:")
                if(num=='q'):
                    needInput=False
                    pass
                elif(num=='h'):
                    print('帮助菜单正在施工')
                elif(num.isalnum()):
                    numN=int(num)
                    if(numN>=0 and numN<=11):
                        card.setRegards(numN)
                        print('给它分配了:'+num)
                    else:
                        print('输入不正确，给你随机分配一个。')
                        randNum=random.randint(0,11)
                        print('给它分配了:'+str(randNum))
                        card.setRegards(randNum)
                    needInput=False
                else:
                    print('输入的内容无法识别，请重新输入！')
    game.sortCard(myCardList)
    if userGotHyphen:
        #os.system("cls") 
        print('为横杠设定好位置后，现在的排序是:')
        game.printAllCards(hisOrHerCardList)
        game.printAllCards(myCardList)
        
    print('谁先开始呢？')
#     print(len(listAllList))
#     card1=card.Card(-1,'w','my',4)
#     card2=card.Card(11,'b','my')
#     list1=[]
#     list1.append(card1)
#     list1.append(card2)
#     game.printAllCards(list1)
#     game.printAllCards(list1)
