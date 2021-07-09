def spinnmin(mat,cor):
    sy,sx,ey,ex=cor
    # print(cor)
    sack=[]
    ru=mat[sy-1][sx-1]
    for i in range(sy,ey):
        mat[i-1][sx-1]=mat[i][sx-1]
        sack.append(mat[i][sx-1])
    for i in range(sx,ex):
        mat[ey-1][i-1]=mat[ey-1][i]
        sack.append(mat[ey-1][i])
    for i in reversed(range(sy,ey)):
        mat[i][ex-1]=mat[i-1][ex-1]
        sack.append(mat[i-1][ex-1])
    for i in reversed(range(sx,ex)):
        mat[sy-1][i]=mat[sy-1][i-1]
        sack.append(mat[sy-1][i-1])
    mat[sy-1][sx]=ru
    sack.append(ru)
    # print(sack,min(sack))
    return mat, min(sack)
def solution(rows, columns, queries):
    answer = []
    # mat=[[0 for i in range(columns)]for j in range(rows)]
    mat=[]
    k=0
    for i in range(rows):
        temp=[]
        for j in range(columns):
            k+=1
            temp.append(k)
        mat.append(temp)
    for k in queries:
        mat,s=spinnmin(mat,k)
        answer.append(s)
    # sy,sx,ey,ex=queries[0]
    # print(mat,sep='\n')
    # print(*mat,queries[0],sep='\n')
    return answer
