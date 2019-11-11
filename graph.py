

class No:

	def __init__(self, nome):
		self.nome = nome
		self.distancia = float('inf')
		self.caminho = []
		self.visitado = False

	def __eq__(self, other):
		return self.nome == other.nome

	def __repr__(self):
		return '{}({} {})'.format(self.nome, self.distancia, self.visitado)


class Aresta:

	def __init__(self, n1, n2, peso):
		self.n1 = n1
		self.n2 = n2
		self.peso = peso

	def __eq__(self, other):
		return self.n1 == other.n1 and self.n2 == other.n2

	def __repr__(self):
		return '{}{}({})'.format(self.n1.nome, self.n2.nome, self.peso)


class Grafo:

	def __init__(self, nos, arestas):
		self.nos = nos
		self.arestas = arestas


	def vizinhos(self, no):
		rn = []
		ra = []
		for a in self.arestas:
			if (a.n1 == no) and (a.n2.visitado == False) and (a.n2 not in rn):
				rn.append(a.n2)
				ra.append(a)

		print('Vizinhos não visitados de', no, rn)
		return rn, ra

	def menor_aresta(self, arestas):
		ma = Aresta(No('X'), No('Y'), float('inf'))

		for a in arestas:
			if a.peso < ma.peso:
				ma = a

		return ma


	def menor_caminho(self, de, para):
		de.distancia = 0
		
		caminho = [de]
		current = de
		de.visitado = True
		de.caminho = [de]
		while current != para:
			
			nos_vizinhos, arestas_vizinhas = self.vizinhos(current)

			for a in arestas_vizinhas:
				if current.distancia + a.peso < a.n2.distancia: 
					a.n2.distancia = current.distancia + a.peso
					a.n2.caminho = current.caminho + [a.n2]

			ma = self.menor_aresta(arestas_vizinhas) # mudar para menor no

			ma.n2.visitado = True

			current = ma.n2
			caminho.append(current)

			print('caminho =', caminho)


		for n in self.nos:
			print(n.distancia)
			print(n.caminho)

			


nA = No('A')
nB = No('B')
nC = No('C')
nD = No('D')
nE = No('E')
nF = No('F')

nos = [nA, nB, nC, nD, nE, nF]

arestas = [
	Aresta(nA, nB, 3),
	Aresta(nB, nA, 3),

	Aresta(nA, nD, 4),
	Aresta(nD, nA, 4),
	
	Aresta(nA, nC, 2),
	Aresta(nC, nA, 2),
	
	Aresta(nB, nD, 2),
	Aresta(nD, nB, 2),

	Aresta(nB, nF, 5),
	Aresta(nF, nB, 5),

	Aresta(nC, nE, 1),
	Aresta(nE, nC, 1),

	Aresta(nD, nE, 1),
	Aresta(nE, nD, 1),

	Aresta(nD, nF, 3),
	Aresta(nF, nD, 3),

	Aresta(nE, nF, 2),
	Aresta(nF, nE, 2),
]

# n1 = No('1')
# n2 = No('2')
# n3 = No('3')
# n4 = No('4')
# n5 = No('5')
# n6 = No('6')

# nos = [n1, n2, n3, n4, n5, n6]

# arestas = [
# 	Aresta(n1, n2, 7),
# 	Aresta(n2, n1, 7),

# 	Aresta(n1, n3, 9),
# 	Aresta(n3, n1, 9),
	
# 	Aresta(n1, n6, 14),
# 	Aresta(n6, n1, 14),
	
# 	Aresta(n2, n3, 10),
# 	Aresta(n3, n2, 10),

# 	Aresta(n2, n4, 15),
# 	Aresta(n4, n2, 15),

# 	Aresta(n3, n4, 11),
# 	Aresta(n4, n3, 11),

# 	Aresta(n3, n6, 2),
# 	Aresta(n6, n3, 2),

# 	Aresta(n4, n5, 6),
# 	Aresta(n5, n4, 6),

# 	Aresta(n5, n6, 9),
# 	Aresta(n6, n5, 9)
# ]

g = Grafo(nos, arestas)
g.menor_caminho(nA, nF)
