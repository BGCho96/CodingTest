def solution(new_id):
    answer = ''
    raw=list(new_id)
    print(new_id)
    f1=[]
    for i in raw:
        if i.isupper():
            f1.append(i.lower())
        else: f1.append(i)
    
    print(''.join(f1))
    f2=[]
    for i in f1:
        if i.isdigit() or i.isalpha() or (i in ['-','_','.']):
            f2.append(i)
    print(''.join(f2))
    f3=[]
    for i in f2:
        if not f3:
            f3.append(i)
            print('처음입력')
        elif not (f3[-1]=='.' and i=='.'):
            f3.append(i)
    print(''.join(f3))
    f4=''.join(f3).strip('.')
    f5='a' if not f4 else f4
    print(f4)
    print(f5)
    f6=f5[:15].strip('.')
    print(f6)
    f7=(f6+f6[-1]*3)[:3] if len(f6)<3 else f6
    print(f7)
    return f7
  # 여유가 되면 이걸 한줄안에 쓰는 기믹도 가능할거 
