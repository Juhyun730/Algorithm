import sys
input = sys.stdin.readline
n=int(input())

stack=[]
for i in range(n):
    l=list(map(int,input().split()))
    if len(l)==2:
        if l[0]==1:
            stack.append(l[1])
    else:
        if l[0]==2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif l[0]==3:
            print(len(stack))
        elif l[0]==4:
            if stack:
                print(0)
            else:
                print(1)
        elif l[0]==5:
            if stack:
                print(stack[-1])
            else:
                print(-1)