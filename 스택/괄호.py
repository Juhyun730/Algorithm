n=int(input())
def a(s):
    stack=[]
    for c in s:
        if c=='(':
            stack.append(c)
        elif c==')':
            if stack:
                stack.pop()
            else:
                return 'NO'
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'
        

for _ in range(n):
    l=list(map(str,input().strip()))
    print(a(l))

