import os

def EngEnc(str, key):
	result = []
	keyLen = len(key)
	i=0
	for char in str:
		result.append(((ord(char) - 65 + key[i]) % 26) + 65)
		if i == (keyLen - 1):
			i = 0
		else:
			i += 1
	return result
			
def EngDec(str, key):
	result = []
	keyLen = len(key)
	i=0
	for char in str:
		result.append(((ord(char) - 65 - key[i]) % 26) + 65)
		if i == (keyLen - 1):
			i = 0
		else:
			i += 1
	return result

a = list("가나다라마")
print(a)
b = print("".join(a))
	
A="UQDPJEFJMFGCIJAJOQBHJSJJOJRMVAHNTQYNZRMXJHUQJTMRBRRFINURNSVYLXQJVADXLRZZPAZYDIFMZDHNSTHSBGINHSQROCHTINOMSMZCSXBQVZBCHTIBGQZSBHMCGJVYQQZGZGPOSMZXPADFIYBWFZVTFKXYCRGREYCPFWSZMLLXQJVANXMFMPIBDOJAHCGJBEFJSNOVTXAXZEWNCTIBDCNGZEORMYCVOBNZOULXQJV"
key=[1,9,25,5,21,13]

plain = ""
for each in EngDec(A,key):
	plain += chr(each)

print(plain)
f = open("c.txt","w")
f.write(plain)
f.close()

os.system("pause")