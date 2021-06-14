from abc import ABC

class CAR(ABC):
	def milege(self):
		pass


class Tesla(CAR):
	def milege(self):
		print("Bahot tez dodti hai...")


s = Tesla()
s.milege()

print(type(s))