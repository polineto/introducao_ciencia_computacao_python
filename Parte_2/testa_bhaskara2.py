import bhaskara2
import pytest # pra funcionar o @pytest.fixture e o @pytest.mark.parametrize

class TestaBhaskara:

    @pytest.fixture
    def b(self):
        return bhaskara2.Bhaskara()

    @pytest.mark.parametrize('entrada, esperado', [
        ( [1,0,0], (1,0) ), #eu tenho que usar [] na entrada pois calcula_raizes recebe três valores de entrada
        ( [1,-5,6], (2,3,2) ), # eu tenho que usar () no esperado pois calcula_raizes tem um saída do tipo ()
        ( [10,10,10], 0 ),
        ( [10,20,10], (1,-1) )
        ])
        

    def testa_raiz(self, b, entrada, esperado):
       #b = bhaskara2.Bhaskara() #nome do módulo = bhaskara2... # nome da classe = Bhaskara
       assert b.calcula_raizes(entrada[0], entrada[1], entrada[2]) == esperado 


'''
b = bhaskara2.Bhaskara() está repetindo demais...
Para evitar isso, nós criamos uma "fixture" passando @pytest.fixture
e definindo uma função...
Depois é só passá-la adiante...
'''


'''
as vezes a quantidade de teste similar é muito grande.
quando isso acontece, eu posso usar a funcao mark.parametrize do modulo pytest
'''


