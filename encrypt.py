import os
import random

class KorChr:
    start = 0
    mid = 0
    end = 0
    def __init__(self,char):
        self.start = (ord(char)-44032) // 588
        self.mid = ((ord(char)-44032) - (588*self.start)) // 28
        self.end = (((ord(char)-44032) - (588*self.start)) - (28*self.mid))
    def __str__(self):
        return "{0},{1},{2},".format(self.start,self.mid,self.end)
    def __str2__(self):
        Start = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        Mid = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        End = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        return "'{0}','{1}','{2}'".format(Start[self.start],Mid[self.mid],End[self.end])
    def Chr(self):
        return chr(44032 + self.start*588 + self.mid*28 + self.end)
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
    
def KeyGen(length):
    key = []
    while len(key) < length:
        key.append(random.randint(1,18))
    return key
    
def Suffler(CipStr):
    result = []
    for char in CipStr:
        result.append(char.start)
    for char in CipStr:
        result.append(char.mid)
    for char in CipStr:
        result.append(char.end)
    return result
    
def Sorter(CipStr):
    length = len(CipStr)//3
    result = []
    temp = []
    for i in range(0,length):
        temp.append(chr(44032 + CipStr[i]*588 + CipStr[i+length]*28 + CipStr[i+2*length]))
    for char in temp:
        result.append(KorChr(char))
    return result
    
def shuffler(lst,order):
    result = []
    i = 0
    j = 0
    try:
        for idx in order:
            result.append(lst[j*len(order) + i])
            if i == len(order) - 1:
                i = 0
                j += 1
            else:
                i += 1
    except IndexError:
        print("오류 발생, 배열의 크기를 벗어남")
        print("i = {0}, j = {1}, 주기의 길이 = {2}".format(i,j,len(order)))
    return result

def TokFreqChk(string,tokLen):
    tmp = list(string)
    tokList = []
    f=open('cipher.txt','a')
    for i in range(len(string)-tokLen+1):
        if tokList.__contains__(tmp[i:i+tokLen:1]) is False:
            tokList.append(tmp[i:i+tokLen:1])
    for tok in tokList:
        print('{0},{1}'.format("".join(tok),string.count("".join(tok))),file=f)
    f.close()

tokLen = 1
while True:
    tokLen = int(input('토큰 길이 : '))
    if tokLen == 0:
        break
    TokFreqChk('wMmYRcDqPJqGYmGjJKtSAmLo♥WzJJtSBpLqUSjJInOtC♡♥♡OsS♥q♣TtBcIyFTp♥sGKuTkKKwN♠mYRvDRmWwN♠mYB♧NgIJqGJwLFbZKzZqS♣♡OAkUwY♣yLO♧PN◇MlKAsRtTKqSRmHk♥sGmYBuFObR♣kUqQ♧TLyKnOAmYSvTAmHmPnOOy♣pPKsSwLxXkUAtBSqEGl♥PnEbMzXp♥wN♠mYRvD♥wNQaYRmYMm♥wLZoBRtBRpQ♣qEIpGePNyWcI♤♣aXPnOAtB♥z♣eUcVKsT♡VkPJqG♣tBRp♥♣yBjEeUcV♠♤♣aXRk♠dOKqG♥nEzFoPmYbBBuZ♣iIYuZKtBcZuEY◇RzARnOZm♥wLZoBRtBSnSvO♠nOsS♣qReE♣tBcJpGqGYrWgGmZLk',tokLen)

os.system('pause')