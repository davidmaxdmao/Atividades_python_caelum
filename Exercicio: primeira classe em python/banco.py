class Banco:
    def __init__(self):
        self._contas = []

    def adiciona(self, conta):
        self._contas.append(conta)

    def pegaConta(self, conta):
        return self._contas.index(conta)

    def pegaTotalContas(self):
        print('total de contas: {}'.format(len(self._contas)))

    @property
    def contas(self):
        return self._contas

# Esta classe foi criada para responder a questão 8 da atividade de herança
# para poder testar é necessário executar um código python com os devidos
# imports de conta, banco e atualizadorDeContas, instanciar algumas contas e um banco para testar,
# como no seguinte códito:
'''
>>> from conta import *
>>> from banco import Banco
>>> from atualizadorDeContas import *

>>> c = Conta(1853,'max',500,1000)
>>> b = Conta(9753,'lulu',500,1000)
>>> a = Conta(123,'david',500,1000)
>>> banese = Banco()
>>> banese.adiciona(c)
>>> banese.adiciona(b)
>>> banese.adiciona(a)
>>> atu = AtualizadorDeContas(123)
>>> for conta in banese.contas:
...     atu.roda(conta, 0.10)

'''