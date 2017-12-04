'''
Created on 2017年12月4日

@author: 魏来
'''
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
    game.printAllCards(hisOrHerCardList)
    game.printAllCards(myCardList)
#     print(len(listAllList))
#     card1=card.Card(-1,'w','my',4)
#     card2=card.Card(11,'b','my')
#     list1=[]
#     list1.append(card1)
#     list1.append(card2)
#     game.printAllCards(list1)
#     game.printAllCards(list1)
