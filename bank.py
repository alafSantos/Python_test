class Pessoa(object):
	def __init__(self, nomeP, cpfP, salarioP):
		self.nome = nomeP
		self.cpf = cpfP
		self.salario = salarioP

	def getSalario(self):
		return self.salario



class ContaBancaria(object):
	def __init__(self, pessoa):
		self.saldo = pessoa.getSalario()
		self.cliente = pessoa
		self.qtdSaques = 0
		self.qtdDepositos = 0

	def saque(self, valor):
		if valor > self.saldo:
			print("Erro: saldo insuficiente!")
		else:
			self.saldo = self.saldo - valor
			self.qtdSaques = self.qtdSaques + 1

	def deposito(self, valor):

		self.saldo = self.saldo + valor
		self.qtdDepositos = self.qtdDepositos + 1


	def mostrarSaldo(self):
		print("Saldo: ",self.saldo)


	def verificaEntrada(self, entrada):
		if entrada < 0 and entrada > -5:
			return (-1)

		if entrada > 0:
			return 1

		if entrada == 0:
			return 0

		else:
			return (-2)


	def saida(self):
		print("Saques: ", self.qtdSaques)
		print("Depositos: ", self.qtdDepositos)
		self.mostrarSaldo()

def main():

     nome = input()
     cpf = input()
     salario = int(input())
     cliente = Pessoa(nome, cpf, salario)
     conta = ContaBancaria(cliente)

     while 1 < 2:
     	valor = int(input())

     	if conta.verificaEntrada(valor) == (-1):
     		break;

     	if conta.verificaEntrada(valor) == (1):
     		conta.deposito(valor)
     		continue

     	if conta.verificaEntrada(valor) == (0):
     		conta.mostrarSaldo()
     		continue

     	if conta.verificaEntrada(valor) == (-2):
     		conta.saque((valor)*(-1))

     conta.saida()

main()
