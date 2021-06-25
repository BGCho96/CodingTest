import sys
sys.setrecursionlimit(10000000)
def GR(N,stat):
    
    if N not in stat:
        stat[N]=N+1
        print(stat)
        return N
    k=GR(stat[N],stat)
    stat[N]=k+1
    
    return k
def solution(k, room_number):
    answer = []
    stat=dict()
    for i in room_number:
        r_n=GR(i,stat)
        answer.append(r_n)
    return answer
