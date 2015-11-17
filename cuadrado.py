class cuadrado:
	def __init__(self, x, y):
	"""Esta función define el cuadrado, lado x, lado y"""
		self.x = x
		self.y = y

	def perimeter(self, x, y):
	"""Esta función calcula el perímetro del cuadrado, la suma de 2 veces cada lado"""
		return (2 * self.x) + (2 * self.y)

