'''숫자 야구(숫자 베이스볼, Number BaseBall 게임을 파이썬으로 구현한 것입니다.'''

import random
import time
import pickle

class score:
    def __init__(self, name, len, trial, spendtime):
        self.Name = name
        self.Hard = len
        self.Time = time.localtime()
        self.Trial = trial
        self.Spend = spendtime
        self.Score = (pow(10,len) - trial) / spendtime

def isoverlap(str):
    for idx in str:
        check = 0
        for idx2 in str:
            if idx2 == idx:
                check += 1
        if check >= 2:
            print('입력하신 문자에 중복되는 숫자가 있습니다. 다시 입력해 주세요.\n')
            return True
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
        trial = 0
        while win == False:
            strike = 0
            ball = 0
            user = input("{}자리 숫자를 입력해 주세요(0 입력 가능) : ".format(length))
            stTime = time.time()
            if len(user) != length or user.isdecimal() == False:
                print('\n잘못 입력하셨습니다. 4자리의 숫자를 입력해 주세요.\n')
                continue

            if isoverlap(user) == True:
                continue
            trial += 1

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
            print('\n축하합니다! 승리하셨습니다. 시도 횟수 : {}'.format(trial))
            name = input('이름을 입력해 주세요. : ')
        endTime = time.time()
        spend = endTime - stTime
        newScore = score(name, length, trial, spend)
        try:
            f = open('Rank.txt','rb')
            rank = pickle.load(f)
        except EOFError:
            print('기록이 존재하지 않습니다. 새로운 데이터베이스를 생성합니다...')
            rank = [newScore]
        except IOError:
            print('기록이 존재하지 않습니다. 새로운 데이터베이스를 생성합니다...')
            rank = [newScore]
            f = open('Rank.txt','wb')
            f.close()
        else:
            idx = 0
            for data in rank:
                if data.Score < newScore.Score:
                    rank.insert(idx,newScore)
                    break 
                else:
                    idx = idx + 1
                    if idx == len(rank):
                        rank.append(newScore)
        finally:
            f.close()
            with open('Rank.txt','wb') as f:
                pickle.dump(rank,f)
        input('종료하시려면 enter 키를 입력해 주세요.')

def ranking():
    try:
        with open('Rank.txt','rb') as f:
            rank = pickle.load(f)
    except EOFError:
        print('플레이 기록이 존재하지 않습니다.')
    else:
        idx = 1
        for data in rank:
            print('{0}위 : {1}, 난이도 : {2} 점수 : {3:.4f}, 시도 횟수 : {4}회, 걸린 시간\
: {5:.2f}초\n'.format(idx, data.Name, data.Hard, data.Score, data.Trial, data.Spend)\
, time.strftime("%Y-%m-%d %I:%M",data.Time))

_version = '0.1.1'
_changelog = '''기록 저장 방법 업데이트. 이제 과거의 기록을 열람할 수 있습니다.
소요 시간 측정 기준을 수정했습니다.'''

numbb()
ranking()
