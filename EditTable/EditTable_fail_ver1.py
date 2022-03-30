import heapq
def solution(n, k, cmd):
    answer = ''
    mostRecent=[]
    table=[i for i in range(n)]
    curPos=k
    answer=['X'for i in range(n)]
    for lines in cmd:
        # print(lines)
        if lines[0]=='U':
            curPos-=int(lines[2])
        if lines[0]=='D':
            curPos+=int(lines[2])
        if lines[0]=='C':
            # 지우고, 다음으로 이동. 단, 다음이 존재하지 않으면 위로(마지막 행일 경우에만 해당)
            mostRecent.append([table.pop(curPos),curPos])
            if curPos==len(table):
                curPos-=1
        if lines[0]=='Z':
            recover,tarPos=mostRecent.pop(-1)
            table.insert(tarPos,recover)
            # heapq.heappush(table,recover)
            if tarPos<curPos:
                curPos+=1
        # for i in range(len(table)):
        #     if curPos==i:
        #         print(table[i],'<-')
        #     else:
        #         print(i)
        # print(mostRecent)
        # print(table)
    for i in table:
        answer[i]='O'
            
        
        
    return ''.join(answer)
  
  
  
