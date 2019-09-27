import abc

class Conta(abc.ABC):
    #criação do atributo da conta

    _total_contas = 0

    #criação de slots
    __slots__ = ['_numero','_titular','_saldo','_limite']

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta._total_contas += 1

    #metodo que retorna o atributo da classe, pode ser usado tanto por um
    #objeto como pela classe em se.
    # devemos lembrar e q além do decorador @classmethod tb temos o
    # @staticmethod que funciona de forma parecida, porém tem suas peculiaridades
    @classmethod
    def get_total_contas(self):
        return Conta._total_contas

#Atividade do capitulo 8, criar metodos de acesso aos atributos
#utilizar __slots__
#criar um atributo da classe para saber quantos objetos foram instanciados

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def limite(self):
        return self._limite

    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo


    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True


    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print('numero: {} \nsaldo:{}'.format(self.numero, self.saldo))

#OBS.: Não criei o método transfere_para(), solicitado na apostila.

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 2)

    def deposita(self, valor):
        self.saldo += (valor - 0.10)

class ContaPoupanca(Conta):

    def __init__(self,numero,titular,saldo,limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 3)