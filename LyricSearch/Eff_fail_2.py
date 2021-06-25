def mkdic(words):
    dictionary=[{} for i in range(max(list(map(len,words))))]
    for i in words:
        for j in range(len(i)):
            if i[:j+1] not in dictionary[j].keys():
                dictionary[j][i[:j+1]]=[i]
            else:
                dictionary[j][i[:j+1]].append(i)
    return dictionary
def mkdicr(words):
    dictionary=[{} for i in range(max(list(map(len,words))))]
    for i in words:
        for j in range(len(i)):
            if i[-j-1:] not in dictionary[j].keys():
                dictionary[j][i[-j-1:]]=[i]
            else:
                dictionary[j][i[-j-1:]].append(i)
    return dictionary
def solution(words, queries):
    answer = []
    a=mkdic(words)
    b=mkdicr(words)
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
        try:
            if pre:
                cand=a[len(js)-1][js]
                for i in cand:
                    if len(i)==len(j):
                        count+=1
            if suf:
                cand=b[len(js)-1][js]
                for i in cand:
                    if len(i)==len(j):
                        count+=1
            if full:
                cand=a[len(js)-1][js]    
                for i in cand:
                    if len(i)==len(j):
                        count+=1
        except: 
            count=0
        answer.append(count)
        
    
    return answer
