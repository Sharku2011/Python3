def pList(self):
	for inner in self:
		if isinstance(inner,list):
			pList(inner)
		else:
			print(inner)