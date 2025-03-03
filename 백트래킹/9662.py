import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
g=[[0]*n for _ in range(n)]
mysum=0
cv=[0]*(n)
rdv=[0]*((2*n)-1)
ruv=[0]*((2*n)-1)
    

def dfs(n,cur_row):
    global mysum
    for i in range(n): # 열
        if 1 not in g[cur_row] and cv[i]==0 and rdv[cur_row-i]==0 and ruv[cur_row+i]==0:
            cv[i]=1
            rdv[cur_row-i]=1
            ruv[cur_row+i]=1
            g[cur_row][i]=1 #방문
            if cur_row==(n-1):
                mysum+=1
            else:
                dfs(n,cur_row+1)
            cv[i]=0
            rdv[cur_row-i]=0
            ruv[cur_row+i]=0
            g[cur_row][i]=0
   

dfs(n,0)
print(mysum)

        


        