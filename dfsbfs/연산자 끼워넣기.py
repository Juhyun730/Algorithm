import sys

input=sys.stdin.readline

mymax=-1e9
mymin=1e9
n=int(input())
l=list(map(int,input().split()))
cal_list=list(map(int,input().split())) # +, -, *, /
#abcd합은 항상 len(l)보다 1작음
def dfs(cal_list,now_total,depth):
    global mymax,mymin
    if depth==n:
        mymax=max(mymax,now_total)
        mymin=min(mymin,now_total)

    if cal_list[0]>=1:
        cal_list[0]-=1
        dfs(cal_list,now_total+l[depth],depth+1)
        cal_list[0]+=1

    if cal_list[1]>=1:
        cal_list[1]-=1
        dfs(cal_list,now_total-l[depth],depth+1)
        cal_list[1]+=1
    
    if cal_list[2]>=1:
        cal_list[2]-=1
        dfs(cal_list,now_total*l[depth],depth+1)
        cal_list[2]+=1

    if cal_list[3]>=1:
        cal_list[3]-=1
        if now_total < 0: 
            dfs(cal_list,-(abs(now_total)//l[depth]),depth+1)
        else:
            dfs(cal_list,now_total//l[depth],depth+1)
        cal_list[3]+=1
        now_total*=l[depth]
    
dfs(cal_list,l[0],1)   


print(int(mymax))
print(int(mymin))