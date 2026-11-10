#gestor_frutas.py
#Projeto: Sistema de Gestão de Frutas e Vendas

class Fruta:
    def __init__(self, id_fruta, tipo, especie, peso):
        self.id = id_fruta
        self.tipo = tipo
        self.especie = especie
        self.peso = peso


class GestorFrutasBase:
    def __init__(self):
        self.frutas = {}
        self.proximo_id = 1

    def mostrar_grelha(self):
        print("\n" + "=" * 60)
        print(" ESTOQUE DISPONÍVEL (GRELHA DE FRUTAS) ")
        print("=" * 60)
        print(f"{'ID':<6} | {'Tipo':<15} | {'Espécie':<15} | {'Peso Disp. (kg)':<15}")
        print("-" * 60)
        if not self.frutas:
            print(" Nenhuma fruta registada no estoque.")
        else:
            for f in self.frutas.values():
                print(f"{f.id:<6} | {f.tipo:<15} | {f.especie:<15} | {f.peso:<15.2f}")
        print("=" * 60 + "\n")