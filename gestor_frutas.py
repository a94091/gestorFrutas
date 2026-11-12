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
        print(" STOCK DISPONÍVEL - GRELHA DE FRUTAS - ")
        print("=" * 60)
        print(f"{'ID':<6} | {'Tipo':<15} | {'Espécie':<15} | {'Peso Disp. (kg)':<15}")
        print("-" * 60)
        if not self.frutas:
            print(" Nenhuma fruta registada no stock.")
        else:
            for f in self.frutas.values():
                print(f"{f.id:<6} | {f.tipo:<15} | {f.especie:<15} | {f.peso:<15.2f}")
        print("=" * 60 + "\n")

    def adicionar_fruta(self):
        print("\n--- ADICIONAR NOVA FRUTA AO STOCK ---")
        tipo = input("Tipo da fruta: ").strip()
        especie = input("Espécie da fruta: ").strip()
        while True:
            try:
                peso = float(input("Peso total para stock(kg): "))
                if peso < 0:
                    print("O peso não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Introduz um numero válido.")

        nova_fruta = Fruta(self.proximo_id, tipo, especie, peso)
        self.frutas[self.proximo_id] = nova_fruta
        print(f"\nFruta '{tipo}' registada com sucesso com o ID: {self.proximo_id}!")
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
            print(f"Tipo: {fruta.tipo}\nEspécie: {fruta.especie}\nPeso em stock: {fruta.peso:.2f} kg")
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

        fruta = self.frutas.get(f_id)
        if not fruta:
            print(f"Fruta com o ID {f_id} não encontrada.")
            return

        print(f"\nA atualizar os dados da fruta ID {f_id}:")
        print("todos os campos são obrigatórios:\n")

        #pede o novo tipo , não aceita deixar vazio
        while True:
            novo_tipo = input("Novo Tipo: ").strip()
            if novo_tipo == "":
                print("Aviso: O tipo não pode ficar vazio! Tenta novamente.")
            else:
                fruta.tipo = novo_tipo
                break

       #pede a nova especie , não aceita deixar vazio
        while True:
            nova_especie = input("Nova Espécie: ").strip()
            if nova_especie == "":
                print("Aviso: A espécie não pode ficar vazia! Tenta novamente.")
            else:
                fruta.especie = nova_especie
                break

        # 4.pede o novo peso não aceita deixar vazio, nem texto, nem zero e negativo
        while True:
            novo_peso = input("Novo Peso em kg: ").strip()
            if novo_peso == "":
                print("O peso não pode ficar vazio!")
                continue

            try:
                peso_valido = float(novo_peso)
                if peso_valido <= 0:
                    print("O peso não pode ser zero e negativo.")
                    continue
                fruta.peso = peso_valido
                break
            except ValueError:
                print("Introduz um número válido.")

        print(f"\nFruta ID {f_id} atualizada com sucesso!")

    def apagar_fruta(self):
        print("\n--- APAGAR FRUTA ---")
        if not self.frutas:
            print("Não existem frutas registadas para apagar.")
            return
        try:
            f_id = int(input("Digita o ID da fruta que vai apagar"))
        except ValueError:
            print("ID inválido")
            return

        if f_id in self.frutas:
            removida = self.frutas.pop(f_id)
            print(f"\n Fruta '{removida.tipo}'(ID:{f_id}) foi removida com sucesso !")
        else:
            print(f"Fruta com o ID {f_id} não encontrada.")
