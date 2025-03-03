import sys
input=sys.stdin.readline

n=int(input())

l=list(map(int,input().split()))

#꼭짓점개수:4
#두면 개수: (n-2)*4+(n-1)*4

#한면 개수: (n-2)*(n-2)+(n-2)*(n-1)*4
n1=((n-2)*(n-2)+(n-2)*(n-1)*4)*min(l)

#합이 가작 작은 두구간
mymin2=2000000
mylist=[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,5],[2,4],[2,5],[3,4],[3,5],[4,5]]
for i in range(12):
    if l[mylist[i][0]]+l[mylist[i][1]]<mymin2:
        mymin2=l[mylist[i][0]]+l[mylist[i][1]]


#합이 가작 작은 세구간
mymin3=3000000
mylist=[[0,1,2],[0,1,3],[0,2,4],[0,3,4],[5,1,2],[5,1,3],[5,2,4],[5,3,4]]
for i in range(8):
    if l[mylist[i][0]]+l[mylist[i][1]]+l[mylist[i][2]]<mymin3:
        mymin3=l[mylist[i][0]]+l[mylist[i][1]]+l[mylist[i][2]]

n2=mymin2*((n-2)*4+(n-1)*4)
n3=mymin3*4
if n==1:
    l.sort()
    print(sum(l[:5]))
    exit(0)
print(n1+n2+n3)

