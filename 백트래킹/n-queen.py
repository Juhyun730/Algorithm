import sys
input=sys.stdin.readline

n=int(input())

v1=[0]*n
v2=[0]*(2*n-1) #왼쪽위에서 오른쪽 아래로 대각선
v3=[0]*(2*n-1) #오른쪽 위에서 왼쪽 아래로 대각선
ans=0

def dfs(x):
    global n, ans
    if x==n:
        ans+=1
        return
    for i in range(n):
        if v1[i]==0 and v2[i-x]==0 and v3[i+x]==0:
                v1[i]=1
                v2[i-x]=1
                v3[i+x]=1
                dfs(x+1)
                v1[i]=0
                v2[i-x]=0
                v3[i+x]=0         


dfs(0)
print(ans)