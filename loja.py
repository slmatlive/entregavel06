"""Classe que guarda os produtos cadastrados."""

from produtos import Produto


class Loja:
    """Uma loja tem vários produtos, mas não é um tipo de produto."""

    def __init__(self, nome):
        self.nome = nome
        self._produtos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome da loja não pode ficar vazio.")
        self._nome = novo_nome.strip()

    @property
    def produtos(self):
        # Devolvo uma tupla para proteger a lista original da loja.
        return tuple(self._produtos)

    def adicionar_produto(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível cadastrar objetos do tipo Produto.")
        if produto in self._produtos:
            raise ValueError(f"Já existe um produto com o código {produto.codigo}.")
        self._produtos.append(produto)

    def gerar_relatorio(self):
        linhas = [f"RELATÓRIO DA {self.nome.upper()}", "-" * 45]

        if not self._produtos:
            linhas.append("Ainda não há produtos cadastrados.")
            return "\n".join(linhas)

        precos = []
        for produto in self._produtos:
            # A mesma chamada funciona para os três tipos de produto.
            preco_final = produto.calcular_preco_final()
            precos.append(preco_final)
            linhas.append(f"{produto.codigo:02d} - {produto.nome}: R$ {preco_final:.2f}")

        linhas.append("-" * 45)
        linhas.append(f"Total de produtos: {len(self._produtos)}")
        linhas.append(f"Menor preço final: R$ {min(precos):.2f}")
        linhas.append(f"Maior preço final: R$ {max(precos):.2f}")
        linhas.append(f"Média de preços: R$ {sum(precos) / len(precos):.2f}")
        return "\n".join(linhas)

    def __str__(self):
        return f"{self.nome} - {len(self._produtos)} produto(s) cadastrado(s)"

    def __repr__(self):
        return f"Loja(nome={self.nome!r}, total={len(self._produtos)})"
