"""Classes dos produtos usadas no sistema da Sprint 6."""

import math
from abc import ABC, abstractmethod


class Produto(ABC):
    """Classe principal. Os tipos de produto vão herdar dela."""

    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        if type(novo_codigo) is not int or novo_codigo <= 0:
            raise ValueError("O código precisa ser um número inteiro positivo.")
        self._codigo = novo_codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome do produto não pode ficar vazio.")
        self._nome = novo_nome.strip()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if (type(novo_preco) not in (int, float)
                or not math.isfinite(novo_preco) or novo_preco < 0):
            raise ValueError("O preço precisa ser um número válido e não negativo.")
        self._preco = float(novo_preco)

    @abstractmethod
    def calcular_preco_final(self):
        """Cada tipo de produto precisa ter sua própria forma de calcular."""
        pass

    def __str__(self):
        return f"{self.codigo} - {self.nome} | Preço: R$ {self.preco:.2f}"

    def __repr__(self):
        return f"{type(self).__name__}(código={self.codigo}, nome={self.nome!r})"

    def __eq__(self, outro):
        # Produtos com o mesmo código são considerados o mesmo cadastro.
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __lt__(self, outro):
        # Isso permite usar sort() para organizar pelo preço final.
        if not isinstance(outro, Produto):
            return NotImplemented
        return (self.calcular_preco_final(), self.codigo) < (
            outro.calcular_preco_final(), outro.codigo
        )


class ProdutoFisico(Produto):
    """Produto que possui peso e tem um valor de frete."""

    def __init__(self, codigo, nome, preco, peso_kg, frete_por_kg=8):
        super().__init__(codigo, nome, preco)
        self.peso_kg = peso_kg
        self.frete_por_kg = frete_por_kg

    @property
    def peso_kg(self):
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, novo_peso):
        if (type(novo_peso) not in (int, float)
                or not math.isfinite(novo_peso) or novo_peso <= 0):
            raise ValueError("O peso precisa ser maior que zero.")
        self._peso_kg = float(novo_peso)

    @property
    def frete_por_kg(self):
        return self._frete_por_kg

    @frete_por_kg.setter
    def frete_por_kg(self, novo_frete):
        if (type(novo_frete) not in (int, float)
                or not math.isfinite(novo_frete) or novo_frete < 0):
            raise ValueError("O valor do frete não pode ser negativo.")
        self._frete_por_kg = float(novo_frete)

    def calcular_preco_final(self):
        return round(self.preco + self.peso_kg * self.frete_por_kg, 2)

    def __str__(self):
        return (f"{self.nome} (físico) | Preço final: "
                f"R$ {self.calcular_preco_final():.2f}")


class ProdutoDigital(Produto):
    """Produto digital que pode receber um desconto."""

    def __init__(self, codigo, nome, preco, desconto_percentual):
        super().__init__(codigo, nome, preco)
        self.desconto_percentual = desconto_percentual

    @property
    def desconto_percentual(self):
        return self._desconto_percentual

    @desconto_percentual.setter
    def desconto_percentual(self, novo_desconto):
        if (type(novo_desconto) not in (int, float)
                or not math.isfinite(novo_desconto)
                or not 0 <= novo_desconto <= 100):
            raise ValueError("O desconto deve ficar entre 0 e 100.")
        self._desconto_percentual = float(novo_desconto)

    def calcular_preco_final(self):
        return round(self.preco * (1 - self.desconto_percentual / 100), 2)

    def __str__(self):
        return (f"{self.nome} (digital) | Preço final: "
                f"R$ {self.calcular_preco_final():.2f}")


class ProdutoPerecivel(Produto):
    """Produto que ganha desconto quando está próximo do vencimento."""

    def __init__(self, codigo, nome, preco, dias_para_vencer):
        super().__init__(codigo, nome, preco)
        self.dias_para_vencer = dias_para_vencer

    @property
    def dias_para_vencer(self):
        return self._dias_para_vencer

    @dias_para_vencer.setter
    def dias_para_vencer(self, novos_dias):
        if type(novos_dias) is not int or novos_dias < 0:
            raise ValueError("Os dias para vencer devem ser um inteiro a partir de zero.")
        self._dias_para_vencer = novos_dias

    def calcular_preco_final(self):
        if self.dias_para_vencer <= 3:
            return round(self.preco * 0.8, 2)
        return round(self.preco, 2)

    def __str__(self):
        return (f"{self.nome} (perecível) | Preço final: "
                f"R$ {self.calcular_preco_final():.2f}")
