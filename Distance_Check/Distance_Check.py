def count(j,k,arr):
    num=0
    if arr[j+1][k]=='P':
        num+=1
    if arr[j-1][k]=='P':
        num+=1
    if arr[j][k+1]=='P':
        num+=1
    if arr[j][k-1]=='P':
        num+=1
    if arr[j][k]=='P':
        num+=1
    return num
def solution(places):
    answer = []
    room_number=len(places)
    room_size=len(places[0])
    pad_size=2
    for i in range(room_number):
        for j in range(room_number):
            places[i][j]=list(places[i][j])
            # print(places[i][j])
            places[i][j].insert(0,'X')
            places[i][j].insert(0,'X')
            places[i][j].append('X')
            places[i][j].append('X')
        places[i].insert(0,['X' for k in range(room_number+pad_size)])
        places[i].insert(0,['X' for k in range(room_number+pad_size)])
        places[i].append(['X' for k in range(room_number+pad_size)])
        places[i].append(['X' for k in range(room_number+pad_size)])
        # print(places[i])
        for j in range(room_number):
            for k in range(room_number):
                if places[i][j][k]=='P':
                    if places[i][j][k+1]=='O':
                        places[i][j][k+1]=1
                    if places[i][j][k-1]=='O':
                        places[i][j][k-1]=1
                    if places[i][j+1][k]=='O':
                        places[i][j+1][k]=1
                    if places[i][j-1][k]=='O':
                        places[i][j-1][k]=1
    for i in range(room_number):
        flag=1
        for j in range(room_number):
            for k in range(room_number):
                if count(j+2,k+2,places[i])>1 and places[i][j+2][k+2]!='X':
                    print('AAAA',i,j,k)
                    flag=0
        answer.append(flag)
    print(places[0])
    return answer
