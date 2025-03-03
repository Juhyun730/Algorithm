import sys
from collections import defaultdict
from itertools import combinations
import bisect
input=sys.stdin.readline

def solution(info, query):
    answer = []
    table=defaultdict(list)
    #info 변환
    for i in info:
        s=i.split()
        score=s.pop()
        for k in range(5):
            combs=combinations(range(4),k)
            for c in combs:
                key=s
                for t in c:
                    key[t]='-'
                table[' '.join(key)].append(int(score))
    for i in table:
        table[i].sort()
    
    #쿼리 변환
    for i in query:
        s=i.replace(" and",'').split()
        score=int(s.pop())
        key=' '.join(s)
        searchlist=table[key]
        if len(searchlist)==0:
            answer.append(0)
            continue
        idx=bisect.bisect_left(searchlist,score)
        answer.append(len(searchlist)-idx)
     
    return answer


    