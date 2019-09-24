class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

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
