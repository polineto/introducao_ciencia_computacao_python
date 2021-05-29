"""Testa a função busca_sequencial"""

import pytest
from busca_sequencial import busca

@pytest.mark.parametrize('lista, elemento, esperado', [
    (['a', 'e', 'i'], 'e', 1),
    ([12, 13, 14], 15, False),
    ([], '', False)
])

def testa_busca(lista, elemento, esperado):
    assert busca(lista, elemento) == esperado
