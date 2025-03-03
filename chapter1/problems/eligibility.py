N = int(input())
for i in range(N):
    person = input().split()
    schoolyear = int(person[1].split('/')[0])
    birthyear = int(person[2].split('/')[0])
    if schoolyear >= 2010 or birthyear >= 1991:
        print(person[0],'eligible')
    elif int(person[-1]) > 40:
        print(person[0],'ineligible')
    else:
        print(person[0],'coach petitions')
        