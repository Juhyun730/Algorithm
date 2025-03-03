l=['zero','one','two','three','four','five','six','seven','eight','nine']

def solution(s):
    answer=''
    i=0

    while i < len(s):
        if ord(s[i])<65:#숫자임
            answer+=str(s[i])
            i+=1
        else:
            for j in l:
                if j in s[i:i+5]:
                    cnt_s=j
                    break
            i+=len(cnt_s)
            idx=l.index(cnt_s)
            answer+=str(idx)

    return answer
s=input()
print(solution(s))