"""Testes simples para verificar as principais regras do programa."""

import unittest

from loja import Loja
from produtos import Produto, ProdutoDigital, ProdutoFisico, ProdutoPerecivel


class TesteSistemaLoja(unittest.TestCase):
    def setUp(self):
        self.fisico = ProdutoFisico(1, "Caderno", 20, 0.5)
        self.digital = ProdutoDigital(2, "E-book", 100, 25)
        self.perecivel = ProdutoPerecivel(3, "Leite", 10, 2)
        self.loja = Loja("Minha loja")

    def test_preco_produto_fisico(self):
        self.assertEqual(self.fisico.calcular_preco_final(), 24)

    def test_preco_produto_digital(self):
        self.assertEqual(self.digital.calcular_preco_final(), 75)

    def test_preco_perecivel_com_desconto(self):
        self.assertEqual(self.perecivel.calcular_preco_final(), 8)

    def test_preco_perecivel_sem_desconto(self):
        produto = ProdutoPerecivel(4, "Pão", 10, 5)
        self.assertEqual(produto.calcular_preco_final(), 10)

    def test_nao_aceita_preco_negativo(self):
        with self.assertRaises(ValueError):
            self.fisico.preco = -1
        self.assertEqual(self.fisico.preco, 20)

    def test_nao_aceita_preco_infinito(self):
        with self.assertRaises(ValueError):
            self.fisico.preco = float("inf")

    def test_nao_aceita_nome_vazio(self):
        with self.assertRaises(ValueError):
            self.digital.nome = " "

    def test_nao_aceita_codigo_invalido(self):
        with self.assertRaises(ValueError):
            self.digital.codigo = 0

    def test_nao_aceita_peso_invalido(self):
        with self.assertRaises(ValueError):
            self.fisico.peso_kg = 0

    def test_nao_aceita_frete_negativo(self):
        with self.assertRaises(ValueError):
            self.fisico.frete_por_kg = -2

    def test_nao_aceita_desconto_maior_que_cem(self):
        with self.assertRaises(ValueError):
            self.digital.desconto_percentual = 101

    def test_nao_aceita_dias_negativos(self):
        with self.assertRaises(ValueError):
            self.perecivel.dias_para_vencer = -1

    def test_nao_instancia_classe_abstrata(self):
        with self.assertRaises(TypeError):
            Produto(5, "Teste", 10)

    def test_impede_codigo_repetido(self):
        self.loja.adicionar_produto(self.fisico)
        with self.assertRaises(ValueError):
            self.loja.adicionar_produto(ProdutoDigital(1, "Outro", 10, 0))

    def test_impede_cadastrar_outro_tipo(self):
        with self.assertRaises(TypeError):
            self.loja.adicionar_produto("Texto qualquer")

    def test_compara_codigo_com_eq(self):
        outro = ProdutoDigital(1, "Arquivo", 20, 10)
        self.assertEqual(self.fisico, outro)

    def test_ordena_com_lt(self):
        produtos = [self.digital, self.fisico, self.perecivel]
        produtos.sort()
        self.assertEqual([p.codigo for p in produtos], [3, 1, 2])

    def test_retorna_tupla_de_produtos(self):
        self.loja.adicionar_produto(self.fisico)
        self.assertIsInstance(self.loja.produtos, tuple)

    def test_relatorio_conta_produtos(self):
        self.loja.adicionar_produto(self.fisico)
        self.loja.adicionar_produto(self.digital)
        texto = self.loja.gerar_relatorio()
        self.assertIn("Total de produtos: 2", texto)
        self.assertIn("Média de preços: R$ 49.50", texto)

    def test_relatorio_loja_vazia(self):
        self.assertIn("Ainda não há produtos", self.loja.gerar_relatorio())

    def test_str_em_todas_as_classes(self):
        for objeto in (self.fisico, self.digital, self.perecivel, self.loja):
            self.assertIsInstance(str(objeto), str)
            self.assertTrue(str(objeto))

    def test_validacao_nome_loja(self):
        with self.assertRaises(ValueError):
            self.loja.nome = ""

    def test_repr(self):
        self.assertIn("ProdutoFisico", repr(self.fisico))
        self.assertIn("Loja", repr(self.loja))


if __name__ == "__main__":
    unittest.main()
