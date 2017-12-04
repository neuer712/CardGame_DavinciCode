'''
Created on 2017年12月4日

@author: 魏来
'''

class Card(object):
    '''
    classdocs
    '''
    lines=['┏━━━━━┑','┃■■■■■│','┃     │','┖─────┘','┏find━┑','┖─new─┘']

    def __init__(self, number,color,belong,*regards):
        self.number=number
        self.color=color
        self.belong=belong
        self.expose=False
        self.isNew=True
        if number <0:
            if len(regards)==1 and type(regards[0])=='int' and regards[0]>=0 and regards[0]<=11 :
                self.regards=regards[0]
            else:
                self.regards=0
        else:self.regards=number
        
    def setRegards(self,regards):
        self.regards=regards
        
    def setBelong(self,belong):
        self.belong=belong
        
    def __cmp__(self,other):
        if(self.regards>other.regards):
            return 1
        elif(self.regards<other.regards):
            return -1
        else:
            return 0
        
    def paintLine(self,n):
        if n==0:
            if self.expose:
                print(self.lines[4],end='')
            else:
                print(self.lines[0],end='')
        elif n==1 or n==3:
            if self.color=='b':
                print(self.lines[1],end='')
            else:
                print(self.lines[2],end='')
        elif n==2:
            if self.belong=='my' or (self.belong!='my' and self.expose):
                if self.number>=0 and self.number<=9:
                    wordToPrint=' '+str(self.number)+' '
                elif self.number<0:
                    wordToPrint=' - '
                elif self.number>=10:
                    if self.color=='b':
                        middleColor='■'
                    else:
                        middleColor=' '
                    wordToPrint=str(self.number//10)+middleColor+str(self.number%10)
                if self.color=='b':
                    print('┃■'+wordToPrint+'■│',end='')
                else:
                    print('┃ '+wordToPrint+' │',end='')
            else:
                if self.color=='b':
                    print(self.lines[1],end='')
                else:
                    print(self.lines[2],end='')
        elif n==4:
            if self.isNew:
                print(self.lines[5],end='')
                self.isNew=False
            else:
                print(self.lines[3],end='')
        
