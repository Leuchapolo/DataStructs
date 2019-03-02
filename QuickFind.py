class QuickFind:
	def __init__(self, n):
		self.n = n
		self.parents = []
		self.sizes = []

		for i in range(n):
			self.parents.append(i)
			self.sizes.append(1)

	def check(self, a, b):
		return self.root(a) == self.root(b)

	def root(self, a):
		while a != self.parents[a]:
			self.parents[a] = self.parents[self.parents[a]]
			a = self.parents[a]
		return a

	def union(self, a, b):
		arrayToChange = -1
		larger, smaller = self.largerThenSmaller(self.root(a), self.root(b))
		if smaller == larger:
			return
		if self.sizes[larger] == self.sizes[smaller]:
			self.sizes[larger] += 1 
		self.parents[smaller] = larger


	def largerThenSmaller(self, rootA, rootB):
		
		if(self.sizes[rootA] > self.sizes[rootB]):
			return rootA, rootB
		return rootB, rootA


qf = QuickFind(10)
qf.union(2,3)
qf.union(3,4)
qf.union(2,3)
qf.union(6,4)
qf.union(2,3)
qf.union(3,4)
qf.union(2,3)
qf.union(3,4)
print(qf.check(2, 3))


