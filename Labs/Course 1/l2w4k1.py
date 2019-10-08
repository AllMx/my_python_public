import hashlib

class Slovr:
    
    
    def __init__(self):
    	pass
    def slov(self, stroka):
        slovrs= {}
        self.inp = stroka.split(' ')
        for i in range(int(len(self.inp)/2)):
            slovrs[self.inp[i*2]] = self.inp[2*i +1]
        return(slovrs)


class Hesh(object):
	hesed = []
	def __init__(self, metod):
		Slovr.__init__(self)
		self.met = metod
	def hsh(self, slovo):
		if self.met == 'md5':
			return (hashlib.md5(slovo.encode()).hexdigest())


if __name__ == '__main__':
	inp1 = 'Barmaley 67 Aibolit 66'
	inp2 = 'md5'
	c = Slovr()
	d = Hesh(inp2)
	cc = c.slov(inp1)

	list_k = list(cc.keys())
	list_k.sort()
	list_h = []

	for i in list_k:
		list_h.append(d.hsh(i))
		print(i, cc[i])
	list_h.sort()

	stra = []

	for o in list_h:
		stra.append(inp2 + " " + str(o))
	print(' '.join(stra))

