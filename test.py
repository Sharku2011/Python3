import os

class arr():
	array = []
	def __init__(self, data):
		self.array = data
	def mult(self):
		for idx in range(0,len(self.array)):
			self.array[idx] *= 2
	def __str__(self):
		return "{}".format(self.array)

def mult(lst):
	for idx in range(0,len(lst)):
		lst[idx] *= 2

a = arr([1,2,3])
a.mult()
print(a)

b = [1,2,3]
mult(b)
print(b)

a=[1,2,3]
for element in range(0,len(a)):
    a[element] *= 2
print(a)
os.system("pause")