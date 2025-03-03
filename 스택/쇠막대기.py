s = input().strip()

stack=[]
result=0

for i in range(len(s)):
    if s[i]=='(':
        stack.append('(')
    else:
        if s[i-1]=='(' : #바로 직전이 ( 이면 레이저임
            stack.pop()
            result+=len(stack)
        else:#바로 직전도 ) 이면 쇠막대기의 끝을 나타냄
            stack.pop()
            result+=1
print(result)