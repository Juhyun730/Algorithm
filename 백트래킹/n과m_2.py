import sys

input=sys.stdin.readline

n,m=map(int,input().split())

visited=[0]*(n+1)
def dfs(x):
    if sum(visited)==m:
        print(' '.join(map(str,cnt)))
    for i in range(x,n+1):
        if visited[i]==0 and sum(visited)!=m:
            visited[i]=1
            cnt.append(i)
            dfs(i+1)
            visited[i]=0
            cnt.remove(i)
cnt=[]
dfs(1)

    




