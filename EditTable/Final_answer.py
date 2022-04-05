import copy
def solution(n, k, cmd):
    answer = ['X'for i in range(n)]
    linkedSack=[]
    nodeMin=0
    nodeMax=n-1
    tomb=[]
    for nodeNum in range(n):
        if nodeNum==nodeMin:
            # if nodeNum==nodeMax:
            #     linkedSack.append([null,null])
            linkedSack.append([-1,nodeNum+1])
        elif nodeNum==nodeMax:
            linkedSack.append([nodeNum-1,-1])
        else : linkedSack.append([nodeNum-1,nodeNum+1])
    for lines in cmd:
        if lines[0]=='U':
            for move in range(int(lines[2:])):
                k=linkedSack[k][0]
        if lines[0]=='D':
            for move in range(int(lines[2:])):
                k=linkedSack[k][1]
        if lines[0]=='C':
            prevIndex=linkedSack[k][0]
            postIndex=linkedSack[k][1]
            tomb.append(k)
            if prevIndex!=-1 and postIndex!=-1:
                linkedSack[prevIndex][1]=postIndex
                linkedSack[postIndex][0]=prevIndex
                k=postIndex
            elif prevIndex==-1:
                linkedSack[postIndex][0]=prevIndex
                k=postIndex
                nodeMin=postIndex
            elif postIndex==-1:
                linkedSack[prevIndex][1]=postIndex
                k=prevIndex
                nodeMax=prevIndex
        if lines[0]=='Z':
            resurrected=tomb.pop(-1)
            prevIndex,postIndex=linkedSack[resurrected]
            # print('resurr',resurrected)
            # print('fix those',linkedSack[prevIndex],linkedSack[postIndex])
            if -1 not in [prevIndex,postIndex]:
                linkedSack[prevIndex][1]=resurrected
                linkedSack[postIndex][0]=resurrected
                # print('fix both')
            elif prevIndex==-1:
                linkedSack[postIndex][0]=resurrected
                # print('fix one')
                nodeMin=resurrected
            elif postIndex==-1:
                linkedSack[prevIndex][1]=resurrected
                # print('fix one')
                nodeMax=resurrected
        # print(lines)
        # for z in range(n):
        #     if z==k:
        #         print(linkedSack[z],'<-')
        #     else: print(linkedSack[z])
        # print(tomb)
    # print(linkedSack)
    print(nodeMin,nodeMax)
    cur=nodeMin
    if cur<0:
        return ''.join(answer)
    while 1:
        # print(cur)
        answer[cur]='O'
        cur=linkedSack[cur][1]
        if cur == -1:
            break
    # print(nodeMin,nodeMax)
    return ''.join(answer)
  
  
  # 바보같은 실수 하지 말자. 반반으로 갈리거나 그 근처에서 말썽 부리면 어이없는 경우로 일반화 실패한거다
