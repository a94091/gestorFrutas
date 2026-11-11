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

    def adicionar_fruta(self):
        print("\n--- ADICIONAR NOVA FRUTA AO ESTOQUE ---")
        tipo = input("Tipo da fruta (ex: Maçã, Laranja): ").strip()
        especie = input("Espécie da fruta (ex: Fuji, Gala): ").strip()
        while True:
            try:
                peso = float(input("Peso total para stock(kg): "))
                if peso < 0:
                    print("O peso não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor, introduz um numero válido.")

        nova_fruta = Fruta(self.proximo_id, tipo, especie, peso)
        self.frutas[self.proximo_id] = nova_fruta
        print(f"\n[OK] Fruta '{tipo}' registada com sucesso com o ID: {self.proximo_id}!")
        self.proximo_id += 1


    def ver_fruta(self):
        print("\n--- CONSULTAR FRUTA POR ID ---")
        if not self.frutas:
            print("Não há frutas no stock")
            return
        try:
            f_id = int(input("Digita o ID da fruta: "))
        except ValueError:
            print("Id inválido.")
            return
        fruta = self.frutas.get(f_id)
        if fruta:
            print("\n" + "-" * 35)
            print(f"DETALHES DA FRUTA [ID: {fruta.id}]")
            print("-" * 35)
            print(f"Tipo: {fruta.tipo}\nEspécie: {fruta.especie}\nPeso em estoque: {fruta.peso:.2f} kg")
            print("-" * 35)
        else:
            print(f"Fruta com o ID {f_id} não encontrada.")

    def atualizar_fruta(self):
        print("\n--- ATUALIZAR FRUTA ---")
        if not self.frutas:
            print("Não há frutas registadas para atualizar.")
            return
        try:
            f_id = int(input("Digita o ID da fruta a atualizar: "))
        except ValueError:
            print("ID inválido.")
            return
        