class uid():
	ID = ""
	PW = ""
	HASH = ""
def __init__(self,id,pw):
	self.ID = id
	self.PW = pw
	self.HASH = hash(id)
	DB = open('db.txt','a')
	print('HASH =',self.HASH,file=DB)
	print('ID =',self.ID,file=DB)
	print('PW =',self.PW,file=DB)
	DB.close()