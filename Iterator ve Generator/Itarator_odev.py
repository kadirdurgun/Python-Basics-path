class Kareler():

	def __init__(self,maksimum):
		self.maksimum = maksimum
		self.index = 1

	def __iter__(self):
		return self

	def __next__(self):


		if ( self.index <= self.maksimum):

			sonuc = self.index ** 2
			self.index += 1

			return sonuc

		else:
			self.index = 1
			raise StopIteration

kare = Kareler(15)
iterator = iter(kare)

for i in kare:
	print(i)


