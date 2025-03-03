import sys
input=sys.stdin.readline

n1=5
n2=5
n3=5
n4=5
n5=5
g=[]
for i in range(10):
    g.append(list(map(int,input().split())))
    
def dfs(x,y,n1,n2,n3,n4,n5):
    for i in range(1,6):
        for attach_x in range(i):
            for attach_y in range(i):
                if g[attach_x][attach_y]==1:
                    g[attach_x][attach_y]=0
for x in range(10):
    for y in range(10):
        if g[x][y]==1:
            dfs(x,y,n1,n2,n3,n4,n5)