def solution(food_times, k):
    answer = 0
    food_num=[i+1 for i in range(len(food_times))]
    # print(food_times, food_num)
    z=0
    while k:
        temp_times=[]
        temp_num=[]
        if k+1>len(food_num):
            # print('여유있음으로 다 먹는다',k,'초')
            # print(food_times)
            for j in range(len(food_times)):
                food_times[j]-=1
                # print(food_times[j])
                if food_times[j]!=0:
                    temp_times.append(food_times[j])
                    temp_num.append(food_num[j])
                # else: print('0 found')
                
            k-=len(food_num)
            
            # print('left',temp_num)
            food_num=temp_num
            food_times=temp_times
            # print(food_times)
        else:
            # print('이젠 아니다',k,'초')
            # print('left',food_num,k)
            return food_num[k]
            break
    return food_num[0]
            
            
    return answer
  '''
  didnt work.
  low efficiency + indexing wasnt so accurate at certain cases.
  could fix the code for better index percision, but code wasnt efficient, not worth fixing.
  

  '''
