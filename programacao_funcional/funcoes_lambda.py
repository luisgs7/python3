compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

if __name__ == '__main__':
    print('Preços totais:', totais)
    print('Total geral:', sum(totais))
