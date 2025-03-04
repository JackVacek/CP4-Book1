from collections import Counter
T=int(input())
for i in range(T):
    n=int(input())
    peeps=[0]*n
    mostVotes=0
    mostVotesIdx=0
    total=0
    for i in range(n):
        num=int(input())
        total+=num
        peeps[i]=num
        if num > mostVotes:
            mostVotes = num
            mostVotesIdx=i+1
    count=Counter(peeps)
    if mostVotes > total//2:
        print("majority winner",mostVotesIdx)
    elif count[mostVotes] != 1:
        print('no winner')
    else:
        print('minority winner',mostVotesIdx)