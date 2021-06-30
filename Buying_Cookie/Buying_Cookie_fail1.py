def cutter(cookie,n):
    left=sum(cookie[:n])
    right=sum(cookie[n:])
    return abs(left-right)
def solution(cookie):
    answer = -1
    # even=sum(cookie)%2==0
    # print(even)
    l_c=len(cookie)
    maxv =l_c-1
    minv=0
    diff=0xFFFF
    count=0
    while diff!=0:
        count+=1
        mid=(minv+maxv)//2
        left=sum(cookie[:mid])
        right=sum(cookie[mid:])
        if mid==minv:
            if cutter(cookie,minv)>cutter(cookie,maxv):
                mid=maxv
                left=sum(cookie[:mid])
                right=sum(cookie[mid:])
            elif cutter(cookie,minv)<cutter(cookie,maxv):
                mid=minv
                left=sum(cookie[:mid])
                right=sum(cookie[mid:])
            break
        
        new_diff=abs(left-right)
        if left<right:
            minv=mid
        elif right<left:
            maxv=mid
        else:
            break
    l=0
    m=mid
    m_p=mid
    r=l_c
    left=cookie[l:m]
    right=cookie[m_p:r]
    while sum(left)!=sum(right):
        if sum(left)<sum(right):
            if right[0]<right[-1]:
                right.pop(0)
            else:
                right.pop(-1)
        if sum(left)>sum(right):
            if left[0]<left[-1]:
                left.pop(0)
            else:
                left.pop(-1)
        if (not left) or (not left):
            break
    print('비었거나 같거나')
    print(left, right)
        
    # print(mid,left,right)
    return sum(left)
