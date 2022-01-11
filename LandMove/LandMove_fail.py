'''
원인 1 : 구획을 먼저 나눠야 한다. 구획 나누기와 사다리 지정을 동시에 할 수는 없다. 구획을 모두 정한 다음에야 어디에 사다리를 놓을지 정할 수 있다.
2 : 전진 방법을 dfs가 아니라 bfs로 해야 한다. 최악의 효율을 보이는 나선 형태를 상상하고 dfs를 했는데, 그게 결국 bfs고 이게 더 빠르다.
해결 과제 : 
1. bfs로 구획을 정하는 알고리즘 작성.
2. 완성된 구획이 생기면 다음 구획의 시작점을 정하는 방법 설정.
3. 모든 구획이 나눠지면 인접구획의 비용 구하는 법 생각할 것. 다익스트라 방법이 그런 알고리즘이였던가.
'''


def solution(land, height):
    answer = 0
    padl=len(land)+2
    start_cord=[1,1]
    stack=[]
    stack.append(start_cord)
    visited=[[99999 for i in range(len(land))]for i in range(len(land))]
    visited[0][0]=1
    newreg=[]
    regindex=1
    for i in land:
        i.append("*")
        i.insert(0,"*")
    land.append(['*' for i in range(padl)])
    land.insert(0,['*' for i in range(padl)])
    # for i in land:
    #     print(i)
    # for i in visited:
    #     print(i)
    z=0
    upcor=[-1,-1,99999]
    dwcor=[-1,-1,-99999]
    while sum(sum(visited,[]))!=0:
        z+=1
        if stack: # 갈곳이 있다면
            now=stack.pop()
            # print(now)
        elif newreg:
            # print('newreg',newreg)
            new=newreg.pop()
            now=new[:2]
            regindex+=1
            visited[now[0]-1][now[1]-1]=regindex
            # for i in visited:
                # print(i)
            
        else:
            if upcor[0]!= (-1) and visited[upcor[1]-1][upcor[0]-1]==99999:
                # print('up exist, insert up')
                # print(upcor,dwcor)
                newreg.append([upcor[1],upcor[0]])
                # print('newreg added',newreg,visited[upcor[1]-1][upcor[0]-1])
                # print('current cands',upcor,dwcor)
                answer+=abs(upcor[2])
                # print(answer)
            upcor=[-1,-1,99999]
            if dwcor[0]!= (-1) and visited[dwcor[1]-1][dwcor[0]-1]==99999:
                # print('dw exist, insert dw')
                # print(upcor,dwcor)
                newreg.append([dwcor[1],dwcor[0]])
                # print('newreg added',newreg,visited[dwcor[1]-1][dwcor[0]-1])
                # print('current cands',upcor,dwcor)
                answer+=abs(dwcor[2])
                # print(answer)
            dwcor=[-1,-1,-99999]
        
            
        goto=[[now[0]+1,now[1]],[now[0]-1,now[1]],[now[0],now[1]-1],[now[0],now[1]+1]]
        # print(goto)
        for y,x in goto:
            # print(y,x)
            
            if land[x][y]!='*' and visited[x-1][y-1]==99999: # 처음가면서
                cost=land[x][y]-land[now[1]][now[0]]
                if (abs(cost)<=height): # 갈수 있는곳
                    # print('cango',cost)
                    stack.append([y,x])
                    visited[x-1][y-1]=regindex
                    # print(upcor[:2])
                    if upcor[:2]==[x,y]:
                        # print('del up')
                        upcor=[-1,-1,99999]
                    if dwcor[:2]==[x,y]:
                        # print('del dw')
                        dwcor=[-1,-1,-99999]
                        
                elif cost<upcor[2] and cost>0:
                    # print(cost,upcor[2],'upstair at',x,y,land[y][x])
                    upcor=[x,y,cost]
                elif cost>dwcor[2] and cost<0:
                    # print('down',x,y,cost)
                    # print(cost,dwcor[2],'dwstair at',x,y,land[y][x])
                    dwcor=[x,y,cost]
                # print('moving to',y,x,land[x][y])
        if z>33333:
            break
    # for i in visited:
        # print(i)
    # print(upcor,dwcor)
    return answer
