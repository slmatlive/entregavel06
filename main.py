"""Exemplo de funcionamento do sistema de loja (Sprint 6)."""

from loja import Loja
from produtos import ProdutoDigital, ProdutoFisico, ProdutoPerecivel


def main():
    loja = Loja("Loja da Sprint 6")

    # Criei 10 produtos para mostrar as classes funcionando.
    produtos = [
        ProdutoFisico(1, "Caderno", 15.50, 0.4),
        ProdutoFisico(2, "Mochila", 90.00, 0.8),
        ProdutoFisico(3, "Lápis", 2.00, 0.1),
        ProdutoFisico(4, "Estojo", 18.00, 0.3),
        ProdutoDigital(5, "E-book de Python", 40.00, 10),
        ProdutoDigital(6, "Curso básico", 120.00, 25),
        ProdutoDigital(7, "Apostila PDF", 18.00, 0),
        ProdutoPerecivel(8, "Leite", 7.50, 1),
        ProdutoPerecivel(9, "Iogurte", 5.00, 2),
        ProdutoPerecivel(10, "Pão", 9.00, 5),
    ]

    for produto in produtos:
        loja.adicionar_produto(produto)

    print("SISTEMA DE PRODUTOS - SPRINT 6")
    print(loja)

    print("\nPOLIMORFISMO: PREÇOS DE CADA TIPO")
    for produto in loja.produtos:
        print(produto)  # O __str__ muda conforme a classe do objeto.

    print("\nORDENAÇÃO PELO PREÇO FINAL")
    produtos_ordenados = list(loja.produtos)
    produtos_ordenados.sort()  # Usa o método especial __lt__.
    for produto in produtos_ordenados:
        print(f"{produto.nome}: R$ {produto.calcular_preco_final():.2f}")

    print("\nEXEMPLO DE __repr__")
    print(repr(produtos[0]))

    print("\nTRATAMENTO DE ERROS")
    try:
        produto_errado = ProdutoFisico(11, "Produto inválido", -10, 1)
        loja.adicionar_produto(produto_errado)
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")

    try:
        loja.adicionar_produto(ProdutoDigital(1, "Código repetido", 20, 5))
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")

    print("\n" + loja.gerar_relatorio())


if __name__ == "__main__":
    main()
