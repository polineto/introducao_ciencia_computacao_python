def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = (i + 1)
    return fat

import pytest

@pytest.mark.parametrize('entrada, esperado',
                         [
                             (0, 1),
                             (1, 1),
                             (-10, 0),
                             (4, 24),
                             (5, 120)
                             ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

#def testa_fatorial0():
#    assert fatorial(0) == 1

#def testa_fatorial1():
#    assert fatorial(1) == 1

#def testa_fatorial_negativo():
#    assert fatorial(-10) == 0

#def testa_fatorial4():
#    assert fatorial(4) == 24

#def testa_fatorial5():
#    assert fatorial(5) == 120

'''
as vezes a quantidade de teste similar é muito grande.
quando isso acontece, eu posso usar a funcao mark.parametrize do modulo pytest
'''
