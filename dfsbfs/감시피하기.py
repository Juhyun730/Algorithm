import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(input())
g=[]
teacher=[]
for i in range(n):
    l=list(map(str,input().split()))
    for j in range(len(l)):
        if l[j]=='T':
            teacher.append([i,j])
    g.append(l)

#일단 장애물을 브루트포스로 넣기
def seto(count):
    if count==3:
        if is_safe():
            print("YES")
            exit()
        return  
    for x in range(n):
        for y in range(n):
            if g[x][y]=='X':
                g[x][y]='O'
                seto(count+1)
                g[x][y]='X'

#선생님의 좌표를 기준으로 학생을 볼 수 있는지 확인하기
def is_safe():
    for x, y in teacher:
        for d in range(4):
            nx=x
            ny=y
            while 0<=nx<n and 0<=ny<n:
                if g[nx][ny]=='O':
                    break
                if g[nx][ny]=='S':
                    return False
                nx+=dx[d]
                ny+=dy[d]

    return True

seto(0)
print('NO')