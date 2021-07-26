PALAVRAS_CHAVE = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]


for texto in textos:
    intersecao = PALAVRAS_CHAVE.intersection(set(texto.lower().split()))

    if intersecao:
        print('Texto possui palavras chaves:', intersecao)
    else:
        print('Texto sem palavras chave:', texto)
