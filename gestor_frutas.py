#gestor_frutas.py
#Projeto: Sistema de Gestão de Frutas e Vendas

class Fruta:
    def __init__(self, id_fruta, tipo, especie, peso):
        self.id = id_fruta
        self.tipo = tipo
        self.especie = especie
        self.peso = peso


class GestorFrutasBase:
    def __init__(frutas):
        self.frutas = {}
        self.proximo_id = 1

        def mostrar_grelha(self):
            print("\n" + "=" * 60)
            print(" ESTOQUE DISPONÍVEL (GRELHA DE FRUTAS) ")
            print("=" * 10)
            print(f"{'ID':<6} | {'Tipo':<15} | {'Espécie':<15} | {'Peso Disp. (kg)':<15}")
            print("-" * 60)
            print("=" * 60 + "\n")