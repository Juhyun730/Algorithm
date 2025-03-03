import sys

input=sys.stdin.readline

l,r=map(str,input().split())
mymin=0

if len(l)==len(r):
    for i in range(len(l)):
        if l[i] != r[i]:
            break
        elif l[i]=='8':
            mymin+=1
else:
    mymin=0


print(mymin)

