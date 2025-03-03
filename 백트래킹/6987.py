import sys
input=sys.stdin.readline
from itertools import combinations
g=[]

for _ in range(4):
    cnt=[]
    s=list(map(int,input().split()))
    for i in range(6):
        cnt.append(s[i*3:(i+1)*3])
    g.append(cnt)

def dfs(num): #num: 몇번째 r경기를 탐색할지//
    global ans
    if num==15:
        for k in range(6):
            if k==5 and l[k][0] ==0 and l[k][1]==0 and l[k][2]==0:
                ans=1
                return 
            elif l[k][0] !=0 or l[k][1]!=0 or l[k][2]!=0:
                break
        return 
    for smp in range(0,3): #승무패
        if smp==0: #a vs b 에서 a가 이겼을때
            #print(l)
            if l[vs[num][0]][smp]>=1 and l[vs[num][1]][2]>=1:
                l[vs[num][0]][smp] -=1
                l[vs[num][1]][2] -=1

                dfs(num+1)
                l[vs[num][0]][smp] +=1
                l[vs[num][1]][2] +=1

        elif smp==1:#a vs b 에서 무승부
            if l[vs[num][0]][smp]>=1 and l[vs[num][1]][smp]>=1:
                l[vs[num][0]][smp] -=1
                l[vs[num][1]][smp] -=1
                #if num==5 and n==0:print(l)
                dfs(num+1)
                l[vs[num][0]][smp] +=1
                l[vs[num][1]][smp] +=1

        elif smp==2: #a vs b 에서 b가 이겼을때
            if l[vs[num][0]][smp]>=1 and l[vs[num][1]][0]>=1:
                l[vs[num][0]][smp] -=1
                l[vs[num][1]][0] -=1

                dfs(num+1)
                
                l[vs[num][0]][smp] +=1
                l[vs[num][1]][0] +=1



vs=list(combinations([0,1,2,3,4,5],2))

for n in range(0,4):
    l=g[n] #n번째 경기
    ans=0
    dfs(0)

    if ans==0:
        print(0,end=' ')
    else:
        print(1,end=' ')


