import conta
import abc
class Tributavel(abc.ABC):
    '''Classe que contém operações  de um objeto autenticável

    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    '''


    @abc.abstractmethod
    def get_valor_imposto(self):
        '''aplica taxa de imposto sobre um determinado valor do objeto'''


Tributavel.register(conta.ContaCorrente)