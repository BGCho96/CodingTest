def solution(words, queries):
    answer = []
    for j in queries:
        pre, suf, full=False,False,False
        if j[-1]=='?':
            pre =True
        if j[0]=='?':
            suf =True
        if j[-1]!='?' and j[0]!='?':
            full=True
        js=j.strip('?')
        count=0
        if pre: 
            for i in words:
                if i.startswith(js) and len(j)==len(i):
                    count+=1
        if suf:
            for i in words:
                if i.endswith(js) and len(j)==len(i):
                    count+=1
        if full:
            for i in words:
                if i==j and len(j)==len(i):
                    count+=1 
        answer.append(count)
                    
        
    
    return answer
  # 효율성 문제로 test case 1,2,3 조짐. 답정너임을 알고 trie 공부 시작
