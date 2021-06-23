class Fila:

	def __init__(self):
		self.fila = []
	
	def insere(self, elemento):
		self.fila.append(elemento)

	def retira(self):
		if not self.vazia():	
			return self.fila.pop(0)

	def tamanho(self):
		return len(self.fila)

	def vazia(self):
		return self.tamanho() == 0

if __name__ == '__main__':
	fila = Fila()
	print(fila.vazia())	
	fila.insere(1)
	fila.insere(2)
	fila.insere(3)
	fila.insere(4)
	fila.insere(5)
	
	print(fila.fila)
	print(fila.vazia())
	print(fila.tamanho())
	
	fila.retira()
	fila.retira()
	fila.insere(6)

	print(fila.fila)
	print(fila.tamanho())