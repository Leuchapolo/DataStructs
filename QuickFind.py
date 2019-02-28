class QuickFind:
	def __init__(self, n):
		self.n = n
		self.parents = []
		for i in range(n):
			self.parents.append(i)

	def check(self, a, b):
		return root(a) == root(b)

	def root(self, a):
		while a != self.parents[a]:
			a = self.parents[a]


	def union(self, a, b):
		self.parents[root(b)] = root(a)



qf = QuickFind(10)
qf.union(2,3)
qf.union(3,4)
print(qf.check(2, 3))
for i in qf.parents:
	print(i)

