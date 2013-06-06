#!/usr/bin/python

class Pessoa:
	_nome = None

	def __init__(self):
		print("Pessoa criada")

	def setNome(self, nome):
		self._nome = nome;
		print("Definido o nome como " +  self._nome);

	def getNome(self):
		print(self._nome);


if( __name__ == '__main__'):
	pessoa = Pessoa()
	pessoa.setNome("Marcelo")
	pessoa.getNome()

