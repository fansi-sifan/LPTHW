from graphics import*
from button import*
from string import*
from random import*
from operator import itemgetter
import re

def addNewWords():
#用户手动添加单词和对应中文解释
    print
    
    wordlist=open("wordlist.txt",'a')

    x=raw_input("Enter the new word: ")
    y=raw_input("Enter the Chinese meaning of the word: ")
    
    while x!="":
        english='%-20s' %x
        chinese='%-20s' %y
        wordlist.write(english+ ' ' +chinese+'0'+'\n')
        
        x=raw_input("Enter another new word: ")
        if x!="":
            y=raw_input("Enter the Chinese meaning of the word: ")
    wordlist.close
    print"the result has been saved to wordlist.txt"
    
def Test():
#程序给出中文，用户输入英文。正确修改fault值，重新保存为文件wordlist
    print
    
    wordlist=open("wordlist.txt",'r')
    lines=wordlist.readlines()
    testNum=input("How many words do you want to test? ")
    while testNum>len(lines):
        testNum=input("Please enter a number smaller than "+str(len(lines))+": ")
    
#检查用户输入是否合法，防止报错
        
    for i in range(testNum):
        line= lines[randrange(0,testNum)]
#随机抽取单词
        
        fault=eval(line[41])
        question=line[21:40]
        question=str.replace(question,' ','')
        
        
        keys=line[0:20]
        keys=str.replace(keys,' ','')
        keys=str.lower(keys)
        
        ans=raw_input("Please enter the translation of "+question+": " )
        ans=str.lower(ans)
        
        if ans==keys:
            print "correct!\n"
            if fault!=0:
                fault=fault-1
        else:
            print "Wrong! The correct answer is: ",keys,"\n"
            fault=fault+1
                        
        line2=line.replace(line[41],str(fault))
        wordlist=open("wordlist.txt",'r')
        final=re.sub(line,line2,wordlist.read())
#使用正则运算，直接在源文件中修改，得到更新fault值后的最终文件
        
        wordlist=open('wordlist.txt','w')
        wordlist.write(final)
        wordlist.close
        
    rep=raw_input("You've finished all the tests!")

def Review():
#程序按照test中错误次数降序排列，供用户复习
    def compare(x,y):
        if x[41]<y[41]:   
            return 1
        elif x[41]>y[41]:
            return -1
        else:
            return 0
    print
    
    wordlist=open("wordlist.txt",'r')
    lines=wordlist.readlines()
    for line in lines:
        lines.sort(cmp=compare)
        print line,
    
    reply=raw_input("\nDo you want to save the result?" )
    if reply[0]=='y' or reply[0]=='Y':
        wordReview=open("wordReview.txt",'w')
        print"the result has been saved to wordReview.txt!"
        for line in lines:
            wordReview.write(line)
    else:
        print"the result has not been saved!"
        
    wordReview.close

def FindWords():
#在给定的四级题库中找出词汇部分的高频词，保存为新文件
    infile = open("2000-2011.txt")
    lines = infile.readlines()
    infile.close()
    
    dictionary = {}
    wordCount = 0
    startSearch = False
    for line in lines:
        if str.find(line, "Part III Vocabulary (") >= 0:
            startSearch = True
        elif str.find(line, "Part IV") >= 0:
            startSearch = False
        #只需要词汇部分
            
        if startSearch and line != "":
            if line[0] == 'A' or line[0] == 'B'\
               or line[0] == 'C' or line[0] == 'D'\
               and line[1] == ')':
                wordCount += 1
                newWord = line[3:-1]
                dictionary[newWord] = 1 + dictionary.get(newWord, 0)

    dictionary = sorted(dictionary.iteritems(),\
                              key = itemgetter(1), \
                              reverse = True)

    outfile = open("result_2000_2010.txt", "w")
    for key, value in dictionary:
        outfile.write('%-20s'%(str(key)) + '%-20s'%(str(value))+ "\n")
    outfile.write("word count: " + str(wordCount) + "\n")
    outfile.write("dictionary length: " + str(len(dictionary)) + "\n")
    outfile.close()
    print"the result has been saved to 'result_2000_2010.txt'!"
   
def memoryWords():
    win=GraphWin("Super-Memory",600,200)
    win.setBackground("White")
    
    banner=Text(Point(300,30),"Super Memory")
    banner.setSize(20)
    banner.setStyle("bold")
    banner.draw(win)
    
    msg=Text(Point(300,80),"Welcome to Super Memory!")
    msg.setSize(16)
    msg.setFill("black")
    msg.draw(win)
    
    bA=Button(win, Point(150,180),120,40,"Add new words")
    bT=Button(win, Point(300,180),120,40,"Test")
    bR=Button(win, Point(450,180),120,40,"Review")
    bF=Button(win, Point(300,130),300,40,"Find most frequent words in CET4")
    bE=Button(win, Point(580,20),30,16,"Exit")
    bA.activate()
    bT.activate()
    bR.activate()
    bF.activate()
    bE.activate()

    while 1:
        p=win.getMouse()
        #等待用户选择执行
        if 90 <= p.getX() <=210 and 160 <= p.getY() <=200:
            addNewWords()         
        if 240 <= p.getX() <=360 and 160 <= p.getY() <=200:
            Test()
        if 390 <= p.getX() <=510 and 160 <= p.getY() <=200:
            Review()
        if 150 <= p.getX() <=450 and 110 <= p.getY() <=150:
            FindWords()
        if 565 <= p.getX() <=595 and 12 <= p.getY() <=28:
            break
            
       
memoryWords()
