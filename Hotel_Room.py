def GR(N,stat):  # N의 숫자를 주면
    # print(stat)
    if stat[N]!=0:  # 방이 빌 때 까지
        for i in range(N,N+stat[N]):  # 얼만큼 뛰어야 하는지 알려주는 함수
            stat[i]+=1
        k=GR(N+stat[N]-1,stat) 
        # print('loop')
        return k
    if stat[N]==0:  # 방이 비었으면 1 해주고 리턴
        stat[N]=1
        return N
def solution(k, room_number):  # 근데 만약 123451 이런식이면 바로 방값이 아니라 여러번의 점프, 함수를 돌게 된다. 이거 때문인가?
    answer = []
    stat={}
    for i in range(k):
        stat[i+1]=0
    for i in room_number:
        temp=GR(i,stat)
        # print('first',temp)
        answer.append(temp)
    # print(stat)
    return answer
