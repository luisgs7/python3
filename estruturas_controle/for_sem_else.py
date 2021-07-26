PALAVRAS_CHAVE = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False

    for palavra in texto.lower().split():
        if palavra in PALAVRAS_CHAVE:
            print('Texto possui pelo menos uma palavra chave:', palavra)
            found = True
            break

    if not found:
        print('Texto sem palavra chave: ', texto)
