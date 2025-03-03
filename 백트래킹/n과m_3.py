import sys

input=sys.stdin.readline

n,m=map(int,input().split())

visited=[0]*(n+1)

def dfs(x):
    if len(cnt)==m:
        print(' '.join(map(str,cnt)))
        return
    for i in range(1,n+1):
        
        #visited[i]=1
        cnt.append(i)
        dfs(i)
        #visited[i]=0
        cnt.pop()
cnt=[]
dfs(1)
