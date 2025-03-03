import sys

input=sys.stdin.readline

n,m=map(int,input().split())
s=[]
def dfs():
    if len(s)==m:
        for j in s:
            print(j,end=' ')
        print('')
    
    for i in range(1,n+1):
        if len(s)<m:
            s.append(i)
            dfs()
            s.pop()
dfs()
        
        