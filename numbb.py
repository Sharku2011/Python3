import random
import time
def isoverlap(str):
    for idx in str:
        check = 0
        for idx2 in str:
            if idx2 == idx:
                check += 1
        if check >= 2:
            print('입력하신 문자에 중복되는 숫자가 있습니다. 다시 입력해 주세요.\n')
            return True
            break
    else:
        return False

def numbb():
    ans = ''
    print('\n##########숫자 베이스볼 게임##########\n')
    length = input("게임을 진행할 자릿수를 정해 주세요(1~10) : ")
    while length.isdecimal() == False:
        length = input("게임을 진행할 자릿수를 정해 주세요(1~10) : ")
    else:
        length = int(length)
    if length > 10 or length < 1:
        print("자릿수는 1과 10 사이의 수가 되어야 합니다.")
    else:
        while len(ans) < length:
            add = '{}'.format(random.randint(0,9))
            if add in ans:
                continue
            else:
                ans = ans + add

        win = False
        count = 0
        stTime = time.time()
        while win == False:
            strike = 0
            ball = 0
            user = input("{}자리 숫자를 입력해 주세요(0 입력 가능) : ".format(length))
            if len(user) != length or user.isdecimal() == False:
                print('\n잘못 입력하셨습니다. 4자리의 숫자를 입력해 주세요.\n')
                continue
            if isoverlap(user) == True:
                continue
            count += 1
            for a in user:
                if a in ans:
                    if ans.find(a) == user.find(a):
                        strike = strike + 1
                    else:
                        ball = ball + 1

            print("\n{0}S, {1}B\n".format(strike,ball))
            if strike == length:
                win = True
        else:
            print('\n축하합니다! 승리하셨습니다. 시도 횟수 : {}'.format(count))
            name = input('이름을 입력해 주세요. : ')
        endTime = time.time()
        spend = endTime - stTime
        now = time.strftime('%Y-%m-%d %H:%M')
        f = open('Rank.txt','a')
        score = '{0}, 걸린 시간 : {1:.0f}초, 시도 횟수 : {2}, 도전자 : {3}\n'.format(now,spend,count,name)
        f.write(score)
        f.close()
        input('종료하시려면 enter 키를 입력해 주세요.')
    
_version = '0.0.3'
_changelog = '경과시간이 자릿수를 정하고 난 뒤부터 지나가도록 변경'

numbb()
