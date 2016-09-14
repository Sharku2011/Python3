import os
import random
import math
import copy

class KorChr:
    start = 0
    mid = 0
    end = 0
    def __init__(self,char):
        self.start = (ord(char)-44032) // 588
        self.mid = ((ord(char)-44032) - (588*self.start)) // 28
        self.end = (((ord(char)-44032) - (588*self.start)) - (28*self.mid))
    def __str2__(self):
        return "{0},{1},{2},".format(self.start,self.mid,self.end)
    def __str__(self):
        Start = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        Mid = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        End = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        return "'{0}','{1}','{2}'".format(Start[self.start],Mid[self.mid],End[self.end])
    def Chr(self):
        return chr(44032 + self.start*588 + self.mid*28 + self.end)
    def Ord(self):
        return (44032 + self.start*588 + self.mid*28 + self.end)
    def Encryptor(self,key):
        self.start += key
        if self.start > 18:
            self.start %= 19
        self.mid += key
        if self.mid > 20:
            self.mid %= 21
        self.end += key
        if self.end > 27:
            self.end %= 28      
    def Decryptor(self,key):
        self.start -= key
        if self.start < 0:
            self.start %= 19
        self.mid -= key
        if self.mid < 0:
            self.mid %= 21
        self.end -= key
        if self.end < 0:
            self.end %= 28

def KeyGen(length):
    key = []
    while len(key) < length:
        key.append(random.randint(1,length-1))
    return key

def Encryptor(str,keys):
    idx = 0
    length = len(keys)
    for char in str:
        char.Encryptor(keys[idx])
        idx += 1
        if idx >= length:
            idx = 0

def Decryptor(str,keys):
    idx = 0
    length = len(keys)
    for char in str:
        char.Decryptor(keys[idx])
        idx += 1
        if idx >= length:
            idx = 0

def RemoveSpace(str):
    temp = list(str)
    for char in temp:
        if ord(char) > 55203 or ord(char) < 44032:
            str = str.replace(char,'')
    return str
    
def Converter(str):
    str = RemoveSpace(str)
    result = []
    for char in str:
        result.append(KorChr(char))
    return result

def Setup(length):
    set = []
    print("암호화용 모판을 생성합니다...")
    print()
    for i in range(0,length):
        row = []
        for i in range(0,length):
            row.append(random.randint(44032,55203))
        set.append(copy.deepcopy(row))
    print("모판 생성이 완료되었습니다.")
    return set

def Chr(cipher,save=False):
    if save is True:
        f = open("cipher.txt","w")
    for row in cipher:
        temp = []
        for i in range(0,len(row)):
            temp.append(chr(row[i]))
        print("".join(temp))
        if save is True:
            print("".join(temp),file=f)
    if save is True:
        f.close()

def Changer(cipher,row,column,data):
    cipher[row][column] = data

def Catcher(cipher,key,plainLen):
    result = []
    cnt = 0
    row = key[0]
    column = 0
    keyLen = len(key)
    order = []
    for pos in key:
        order.append(pos)
    if key[keyLen-1] >= keyLen//2:
        order.append(0)
    else:
        order.append(keyLen-1)
    print("암호 키에 따라 은닉되어 있는 암호문을 수집하고 있습니다...")
    while cnt < plainLen:
        while row != order[column+1]:
            if cnt == plainLen:
                break
            result.append(KorChr(chr(cipher[row][column])))
            cnt += 1
            if order[column+1]-order[column] > 0:
                row += 1
            else:
                if (order[column+1]-order[column]) < 0:
                    row -= 1
        if cnt == plainLen:
            break
        result.append(KorChr(chr(cipher[row][column])))
        cnt += 1
        column += 1
    print()
    print("암호문 수집이 완료되었습니다.")
    print()
    return result

def TransPlanter(cipher,key,plainLen):
    result = []
    cnt = 0
    row = key[0]
    column = 0
    keyLen = len(key)
    order = []
    for pos in key:
        order.append(pos)
    if key[keyLen-1] >= keyLen//2:
        order.append(0)
    else:
        order.append(keyLen-1)
    print("암호문을 모판에 은닉중입니다...")
    while cnt < plainLen:
        while row != order[column+1]:
            if cnt == plainLen:
                break
            cipher[row][column] = temp[cnt].Ord()
            cnt += 1
            if order[column+1]-order[column] > 0:
                row += 1
            else:
                if (order[column+1]-order[column]) < 0:
                    row -= 1
        if cnt == plainLen:
            break
        cipher[row][column] = temp[cnt].Ord()
        cnt += 1
        column += 1
    print()
    print("은닉이 완료되었습니다.")
    print()
    return result

plain = RemoveSpace(input("평문을 입력하시오 : \n"))
print("\n정리된 평문 :\n",plain)
plainLen = len(plain)

print("\n평문 길이 : ",plainLen)
print()
keyLen = int(math.sqrt(plainLen)) * 2
print("키 길이 : ",keyLen)
print()
print("키를 생성중입니다...")
key = KeyGen(keyLen)
print()
#key = [5,2,9,13,0,12,0,12,2,13,1,6,0,13]
checksum = []

while True:
    checksum = []
    for idx in range(0,keyLen-1):
        checksum.append(abs(key[idx+1]-key[idx])+1)
    if sum(checksum) + key[keyLen-1] < plainLen:
        key = KeyGen(keyLen)
    else:
        break
print("키 생성이 완료되었습니다.")
print()
print("암호키 :",key)  #암호키 출력

cipher = Setup(keyLen)  #암호화용 판 생성
Chr(cipher)
print()
temp = Converter(plain)

print("평문을 1차적으로 비즈네르 암호화 하는 중입니다...")
Encryptor(temp,key)

print()
print("암호문 :")
for char in temp:
    print(char.Chr(),end="")

print("\n")

TransPlanter(cipher,key,plainLen)

print("최종 암호문 : ")
print()
Chr(cipher,True)        #암호문 출력 부분
print()

print("복호화를 시작합니다.")

str = Catcher(cipher,key,plainLen)

print("은닉 되어있던 암호문 : ")
print()
for i in str:
    print(i.Chr(),end="")
print()
print()

print("찾아낸 암호문을 복호화 합니다...")
Decryptor(str,key)

print("복호화가 완료되었습니다.")
print()
print("해독된 평문 : ")
print()
for i in str:
    print(i.Chr(),end="")
print()

print(__name__)
os.system("pause")