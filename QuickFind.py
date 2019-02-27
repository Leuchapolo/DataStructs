class QuickFind:
	def __init__(self, n):
		self.n = n
		self.parents = []
		for i in range(n):
			self.parents.append(i)
	def check(self, a, b):
		if(a >= self.n or b >= self.n):
			print("Input out of range")
			return
		rootA,rootB = (-1,-1)
		currentA, currentB = (a, b)
		while (rootA == -1 or rootB == -1):
			if( currentA == self.parents[currentA]):
				rootA = currentA
			else: 
				currentA = self.parents[currentA]
			if(currentB == self.parents[currentB]):
				rootB = currentB
			else: 
				currentB = self.parents[currentB]
		if(rootA == rootB):
			return True
		else:
			return False
	def union(self, a, b):
		self.parents[b] = a



qf = QuickFind(10)
qf.union(2,3)
qf.union(3,4)
print(qf.check(2, 3))
for i in qf.parents:
	print(i)

