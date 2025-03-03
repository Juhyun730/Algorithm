import sys

input=sys.stdin.readline

a,b=map(int,input().split())
g=[1]*(b+1)
g[0]=0
g[1]=0

for num in range(2,int((b+1)**(1/2))+1):
    if g[num]==1:
        for k in range(num*2,b+1,num):
            g[k]=0


mysum=0
#4,6,8,9,10
for n in range(a,b+1):
    if g[n]==0:
        temp=0
        i=2
        cnt_n=n
        while True:
            if g[cnt_n]==1:
                temp+=1
                break
            elif g[i]==1:
                if cnt_n%i==0:
                    temp+=1
                    cnt_n=cnt_n//i
                else:
                    i+=1
            else:
                i+=1
        if g[temp]:
            mysum+=1

print(mysum)
