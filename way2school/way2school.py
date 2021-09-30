def solution(m, n, puddles):
    answer = 0
    Map=[[0 for i in range(m)] for i in range(n)]
    
    for x,y in puddles:
        Map[y-1][x-1]='X'
    for i in range(m):
        if Map[0][i]!='X':
            Map[0][i]=1
        else:
            break
    for i in range(n):
        if Map[i][0]!='X':
            Map[i][0]=1
        else:
            break
    for j in range(1,m):
        for i in range(1,n):
            # print('doing',i,j)
            if Map[i-1][j]!='X':
                a=Map[i-1][j]
                # print('a',a)
            else: 
                a=0
                # print('X')
            if Map[i][j-1]!='X':
                b=Map[i][j-1]
                # print('b',b)
            else: 
                b=0
                # print('X')
            if Map[i][j]!='X':
                Map[i][j]=a+b
                # print('a+b',a,b)
            # else: print('X')
                
            
    # print(Map)
    return Map[-1][-1]%1000000007
