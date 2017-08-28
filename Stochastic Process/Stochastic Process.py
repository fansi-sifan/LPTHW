import numpy as np
import matplotlib.pyplot as plt

def SP():
   steps=input("������������̵Ĳ���: ")
            
   s=np.random.randn(1,steps) #�õ���̬�ֲ�����N��0,1����1ά�������
   p=np.cumsum(s) #�����������

   plt.plot(p)
   plt.show()

def SDE():
   N=input ("������������̵Ĳ�����")
   s0=input ("���������������ʼλ�õ�ֵ��")
   Alpha,Mu,Sigma=input ("����������Alpha,Mu,Sigma��ֵ: ")
  
   S=np.zeros(N+1)
   S[0]=s0
   dt=0.02 #ȡ�㹻С��dt�����е���
   
   for i in range (0,N):
      dBt=np.sqrt(dt)*np.random.randn() #�õ�����N(0,dt)�������
      S[i+1]=S[i]+Alpha*(Mu-S[i])*dt+Sigma*S[i]*dBt #����
   plt.plot(S,label='Alpha=%s \nMu=%s \nSigma=%s'%(Alpha,Mu,Sigma))  
   plt.text(N/10,np.min(S),'Mean=%0.2f \nDev=%0.2f'%(np.mean(S),np.var(S))) #��ʾ�����ͷ���

   plt.legend()
   plt.show()
   
SDE()
def main():
   plt.title('������̴���ҵ ��˼��')
   plt.xlabel('time')
   plt.ylabel('position')
   
   if input("������Ҫ���е���ţ�1��2��: ")==1:
      SP()
   else:
      SDE()





