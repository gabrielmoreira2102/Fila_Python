class Fila (object):

	def __init__(self):
		self.dados = []
	
	def insere(self, elemento):
		self.dados.append(elemento)

	def retira(self):
		return self.dados.pop(0)

	def vazia(self):
		return len(self.dados) == 0

if __name__ == '__Fila__':
	fila = Fila()
	fila.insere(1)
	fila.insere(2)
	fila.insere(3)
	fila.insere(4)
	fila.insere(5)

	print(fila.dados)

	fila.retira()
	fila.retira()
	fila.insere(6)

	print(fila.dados)