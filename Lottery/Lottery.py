"""
git push/pull testin

"""
def solution(lottos, win_nums):
    answer = []
    eq_num=0
    joker=0
    prize=6
    for i in lottos:
        if i in win_nums:
            eq_num+=1
        if i==0:
            joker+=1
    print(eq_num,joker)
    best=prize-eq_num-(joker-1)
    worst=prize-eq_num-(-1)
    if best>6:
        best=6
    if worst>6:
        worst=6
    return [best,worst]
