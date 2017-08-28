import numpy as np
import matplotlib.pyplot as plt

def SP():
   steps=input("请输入随机过程的步数: ")
            
   s=np.random.randn(1,steps) #得到正态分布符合N（0,1）的1维随机数组
   p=np.cumsum(s) #对随机数迭代

   plt.plot(p)
   plt.show()

def SDE():
   N=input ("请输入随机过程的步数：")
   s0=input ("请输入随机过程起始位置的值：")
   Alpha,Mu,Sigma=input ("请依次输入Alpha,Mu,Sigma的值: ")
  
   S=np.zeros(N+1)
   S[0]=s0
   dt=0.02 #取足够小的dt，进行迭代
   
   for i in range (0,N):
      dBt=np.sqrt(dt)*np.random.randn() #得到符合N(0,dt)的随机数
      S[i+1]=S[i]+Alpha*(Mu-S[i])*dt+Sigma*S[i]*dBt #迭代
   plt.plot(S,label='Alpha=%s \nMu=%s \nSigma=%s'%(Alpha,Mu,Sigma))  
   plt.text(N/10,np.min(S),'Mean=%0.2f \nDev=%0.2f'%(np.mean(S),np.var(S))) #显示期望和方差

   plt.legend()
   plt.show()
   
SDE()
def main():
   plt.title('随机过程大作业 刘思凡')
   plt.xlabel('time')
   plt.ylabel('position')
   
   if input("请输入要进行的题号（1或2）: ")==1:
      SP()
   else:
      SDE()





