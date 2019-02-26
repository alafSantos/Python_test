class Vagao(object):
	def __init__(self, carga):
		self.peso = carga

	def getPeso(self):
		return self.peso


class Trem(object):
	def __init__(self, pesoMax):
		self.capMaxPeso = pesoMax
		self.vagoes = []

	def getPesoAtual(self):
		contador = 0
		pesoAtual = 0
		while contador < len(self.vagoes):
			pesoAtual = pesoAtual + self.vagoes[contador].getPeso()
			contador = contador + 1
		return pesoAtual

	def verificaCarga(self, peso):
		if peso == 0:
			return 0

		if peso+self.getPesoAtual() > self.capMaxPeso:
			print("Erro")
			return 0

		if peso < 0:
			return (-1)

		else:
			return 1


	def addVagao(self, cargueiro):
		self.vagoes.append(cargueiro)

	def saida(self):
		print("Numero de vagoes: ", len(self.vagoes))
		print("Peso total: ", self.getPesoAtual())

def main():

    pesoMax = int(input())
    thomas = Trem(pesoMax)

    while 1 < 2:
    	pesoVagao = int(input())

    	if thomas.verificaCarga(pesoVagao) == 0:
    		continue
    	elif thomas.verificaCarga(pesoVagao) == (-1):
    		break
    	else:
    		cargueiro = Vagao(pesoVagao)
    		thomas.addVagao(cargueiro)

    thomas.saida()

main()
