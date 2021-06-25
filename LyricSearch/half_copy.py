def make_trie(words):
    trie={}
    
    for word in words:
        l=len(word)
        cur=trie
        for ch in word:
            if ch in cur:
                cur=cur[ch]
                cur['0'].append(l)             
            else:
                cur[ch]={}
                cur=cur[ch]
                cur['0']=[l]
    return trie
def solution(words, queries):
    answer = []
    
    rev_words, counted = [], []   # 조건 b, c를 위한 두 변수
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w)) 

    trie = make_trie(words)   # 조건 a 의 trie
    rev_trie = make_trie(rev_words)   #조건 b 의 rev_trie 
    for q in queries:
        if q[0]=='?' and q[-1]=='?':
            count=counted.count(len(q))
        elif q[0]!='?':
            pos=trie
            for u in q:
                count=0
                if u=='?':
                    count = pos['0'].count(len(q))
                    # print(count, pos['0'])
                    break
                elif u in pos:
                    pos=pos[u]
                else:
                    count=0
                    break
        elif q[-1]!='?':
            pos=rev_trie
            for u in q[::-1]:
                count=0
                if u=='?':
                    count = pos['0'].count(len(q))
                    # print(count, pos['0'])
                    break
                elif u in pos:
                    pos=pos[u]
                else:
                    count=0
                    break
        answer.append(count)
    # print(trie)
    return answer
