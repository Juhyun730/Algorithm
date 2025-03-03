import sys

n,m=map(int,input().split())

l=list(map(int,input().split()))

l.sort()
cnt=[]
visited=[0]*n

def dfs(start):
    if len(cnt)==m:
        print(*cnt)
        return
    
    flag=0
    for i in range(start,n): #cnt의 i번째 수를 고르는 과정
        if visited[i]==0 and flag!=l[i]:
            visited[i]=1
            cnt.append(l[i])
            print("###",flag)
            flag=l[i]
            print(flag)
            dfs(start+1)
            cnt.pop()
            visited[i]=0

dfs(0)