def solution(enroll, referral, seller, amount):
    answer = []
    invite={}
    paycheck={}
    for i in range(len(enroll)):
        if referral[i]!='-':
            invite[enroll[i]]=referral[i]
        else:
            invite[enroll[i]]='center'
        paycheck[enroll[i]]=0
    # print(invite,paycheck)
    for i in range(len(seller)):
        
        income=amount[i]*100
        paycheck[seller[i]]+=income
        # print('입금',seller[i],paycheck[seller[i]])
        invtee=seller[i]
        while True:
            under=invtee
            invtee=invite[invtee]
            if invtee=='center':
                income=income//10
                paycheck[under]-=income
                break
            else:
                income=income//10
                paycheck[under]-=income
                # print('출금',under,paycheck[under])
                paycheck[invtee]+=income
                # print('부수입',invtee,paycheck[invtee])
            if income==0:
                break
    for i in range(len(enroll)):
        answer.append(paycheck[enroll[i]])
    return answer
