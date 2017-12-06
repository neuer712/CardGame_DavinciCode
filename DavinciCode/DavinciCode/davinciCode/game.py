'''
Created on 2017年12月4日

@author: 魏来
'''
from davinciCode import card
import functools

def printAllCardsStep(cardList,n):
    for card in cardList:
        card.paintLine(n)
        print('   ',end='')
        
    print('')
    
def printAllCards(cardList):
    i=0
    while(i<=4):
        printAllCardsStep(cardList, i)
        i+=1
        
def prepareCards(preparedCardList,myCardList,hisOrHerCardList):
    i=0
    while i<=3:
        currentCard=preparedCardList.pop()
        currentCard.setBelong('my')
        myCardList.append(currentCard)
        i+=1
    while i<=7:
        currentCard=preparedCardList.pop()
        currentCard.setBelong('hisOrHer')
        hisOrHerCardList.append(currentCard)
        i+=1
    sortCard(myCardList)
    sortCard(hisOrHerCardList)
    
def sortCard(listToSort):
    listToSort.sort(key=lambda x: (x.regards,x.color,x.number))