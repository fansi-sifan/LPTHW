from graphics import *
from random import random
import math

def main():
    times=input("How many times to play? ")
    win=GraphWin("St. Petersburg paradox",1400,500)
    win.setCoords(0.0, 0.0, times, 40.0)
    Text(Point(20.0/1500*times,20),"20").draw(win)#���������Ĳ�����
    Text(Point(times*0.95,1),times).draw(win)
    win.setBackground("white")
    
    total=0
    for i in range(times+1):
        n=0
        money=0
        e=0
             
        while random()>0.5:
            n=n+1
            money=money+2**(n)#����һ�������������
            
        total=total+money#��������ģ�������������
        e=float(total)/float(i+1)#���������ƽ���������ѧ����

        P1=Point(i+1,math.log(i+1)/math.log(2))#��㻭��������lnx/ln2
        P1.setFill("red")
        P1.draw(win)
        
        P2=Point(i+1,e)#��㻭ģ������
        P2.setFill("blue")
        P2.draw(win)
        
    win.getMouse()
    win.close()
main()

    
    
