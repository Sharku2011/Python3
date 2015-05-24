'''인간, 오크, 네크론 3종족중 원하는 클래스의 객체를 만들어서 db.txt 파일에 저장하는 프로그램'''
class creature:
	def __init__(self,race,pop=100,breed=0,tech=0):
		self.Race = race
		self.Population = pop
		self.Breed = breed
		self.Tech = tech
	def breed(self):
		if self.Population >= 2:
			self.Population = self.Population*(self.Breed+1)
			print('번식을 통해 인구수가 증가했습니다!')
			print('번식 후 인구 : {}'.format(self.Population))
		else:
			self.Population = 0
			print('번식할 만한 인구가 없습니다.')
	def death(self):
		if self.Population > 0:
			origin = self.Population
			self.Population = origin - int(origin*self.Tech/10)
			print('{0}명의 인구가 늙어 죽었습니다.'.format(int(origin*self.Tech/10)))
			print('남은 인구 : {}'.format(self.Population))
			
check = False
RACE = ('Human','Orc','Necron')
while check == False:
	race = input('Set your race(Human,Orc,Necron): ')
	if race in RACE:
		check = True
	else:
		print('종족명은 Human, Orc, Necron 중 하나가 되어야 합니다.')
else:
	check = False
while check == False:
	pop = int(input('Set your population(bigger than 0) : '))
	if pop > 0:
		check = True
else:
	check = False
while check == False:
	breed = int(input('Set your breeding speed(0~2) : '))
	if breed >= 0 and breed <= 2:
		check = True
else:
	check = False
while check == False:
	tech = int(input('Set your technology(0~2) : '))
	if tech >= 0 and tech <= 2:
		check = True
myTribe = creature(race,pop,breed,tech)
print(myTribe.Race,myTribe.Population,myTribe.Breed,myTribe.Tech)
import pickle
db = 'db.txt'
f = open(db,'wb')
pickle.dump(myTribe,f)
f.close()
f = open(db,'rb')
savedTribe = pickle.load(f)
print(f)
savedTribe.breed()
savedTribe.death()
f.close()