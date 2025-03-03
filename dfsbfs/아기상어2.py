import sys
from collections import deque
input =sys.stdin.readline
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())

dx=[0,0,1,-1,-1,-1,1,1]
dy=[1,-1,0,0,-1,1,-1,1]

g=[]
for i in range(n):
    g.append(list(map(int,input().split())))


def fun1(x,y):
    for v in range(8):
        nx=dx[v]+x
        ny=dy[v]+y
        if 0<=nx<n and 0<=ny<m and g[nx][ny]==0:
            continue
        elif 0<=nx<n and 0<=ny<m and g[nx][ny]==1:
            return False
    return True

def dfs(x,y,depth):
    global mysum
    #깊이에 따른 탐색 범위
    depth_up_start_x=x-depth
    depth_up_end_x=x-depth
    depth_up_start_y=y-depth
    depth_up_end_y=y+depth
    
    depth_down_start_x=x+depth
    depth_down_end_x=x+depth
    depth_down_start_y=y-depth
    depth_down_end_y=y+depth
    num1=[]
    num2=[]
    num3=[]
    num4=[]
    if 0<=depth_up_start_x<n :
        if 0<=depth_up_start_y<m:
            num1=fun1v[depth_up_start_x][depth_up_start_y:depth_up_end_y+1]
        else:
            num1=fun1v[depth_up_start_x][:depth_up_end_y+1]

    if 0<=depth_down_start_x<n :
        if 0<=depth_down_start_y<m:
            num3 = fun1v[depth_down_start_x][depth_down_start_y:depth_down_end_y+1]
        else:
             num3 = fun1v[depth_down_start_x][depth_down_start_y:]
    num2=[]
    num4=[]
    for ii in range(depth_up_start_x,depth_down_start_x+1):
        if 0<=ii <m and 0<=depth_down_start_y<m:
            num2.append(fun1v[ii][depth_down_start_y])
        if 0<=ii <m and 0<=depth_down_end_y<m:
            num4.append(fun1v[ii][depth_down_end_y])
    print(depth_down_end_y)       
    print(num4)
    if len(num1)!=0:
        if False in num1:
            return mysum
    if len(num2)!=0:
        if False in num2:
            return 
    if len(num3)!=0:
        if False in num3:
            return mysum    
    if len(num4)!=0:
        if False in num4:
            return mysum
    mysum+=1
    dfs(x,y,depth+1)


fun1v=[[0]*m for _ in range(n)]

realsum=0
for x in range(n):
    for y in range(m):
        fun1v[x][y]=fun1(x,y)

for x in range(n):
    for y in range(m):
        if g[x][y]==0 and fun1(x,y)==True:
            mysum=0
            dfs(x,y,1)
            realsum=max(realsum,mysum)

print(realsum)