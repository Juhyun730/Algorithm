s=input()

ans0=0
ans1=0

i=0
while i<len(s):
    if s[i]=='0':
        cnt=s[i]
        for k in s[i+1:]:
            if k=='0':
                cnt=cnt+k
            else:
                break
        i+=len(cnt)
        ans0+=1
    elif s[i]=='1':
        cnt=s[i]
        for k in s[i+1:]:
            if k=='1':
                cnt=cnt+k
            else:
                break
        i+=len(cnt)
        ans1+=1


print(min(ans1,ans0))