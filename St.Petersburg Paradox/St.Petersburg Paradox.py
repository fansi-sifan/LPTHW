from graphics import *
from random import random
import math

def main():
    times=input("How many times to play? ")
    win=GraphWin("St. Petersburg paradox",1400,500)
    win.setCoords(0.0, 0.0, times, 40.0)
    Text(Point(20.0/1500*times,20),"20").draw(win)#收益期望的参照量
    Text(Point(times*0.95,1),times).draw(win)
    win.setBackground("white")
    
    total=0
    for i in range(times+1):
        n=0
        money=0
        e=0
             
        while random()>0.5:
            n=n+1
            money=money+2**(n)#储存一次试验的总收益
            
        total=total+money#储存所有模拟试验的总收益
        e=float(total)/float(i+1)#计算出总体平均收益的数学期望

        P1=Point(i+1,math.log(i+1)/math.log(2))#描点画参照曲线lnx/ln2
        P1.setFill("red")
        P1.draw(win)
        
        P2=Point(i+1,e)#描点画模拟曲线
        P2.setFill("blue")
        P2.draw(win)
        
    win.getMouse()
    win.close()
main()

    
    
