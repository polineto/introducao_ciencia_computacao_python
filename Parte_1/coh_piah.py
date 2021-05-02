import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    Sim = 0
    for i in range(len(as_a)):
        Sim += abs(as_a[i] - as_b[i])
    
    return Sim / 6


def conta_caracteres(elemento):
    n_caracteres = 0
    for elem in elemento:
        n_caracteres += len(elem)

    return n_caracteres
        

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto) 

    lista_frases = []
    for sentenca in lista_sentencas:
        frases = separa_frases(sentenca)
        lista_frases.extend(frases)

    lista_palavras = []
    for frase in lista_frases:
        palavras = separa_palavras(frase)
        lista_palavras.extend(palavras)

    new_wal = conta_caracteres(lista_palavras) / len(lista_palavras) 
    new_ttr = n_palavras_diferentes(lista_palavras) / len(lista_palavras) 
    new_hlr = n_palavras_unicas(lista_palavras) / len(lista_palavras) 
    new_sal = conta_caracteres(lista_sentencas) / len(lista_sentencas) 
    new_sac = len(lista_frases) / len(lista_sentencas) 
    new_pal = conta_caracteres(lista_frases) / len(lista_frases) 

    
    return [new_wal, new_ttr, new_hlr, new_sal, new_sac, new_pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    similaridades = []
    for assinatura in assinaturas:
        Sim = compara_assinatura(assinatura, ass_cp)
        similaridades.append(Sim)

    aluno = (similaridades.index(min(similaridades)) + 1)
        
    return aluno


def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    print("O autor do texto ", avalia_textos(textos, ass_cp), " está infectado com COH-PIAH")

