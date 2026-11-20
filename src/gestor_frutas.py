#gestor_frutas.py
#Projeto: Sistema de Gestão de Frutas e Vendas


"""Sistema de Gestão de Frutas e Vendas em terminal (CLI).

:Date: nov, 2026
:Version: 1.2
:Authors: Artur Ferreira, Daniel Mikhelyev, Tómas Massano
"""

class Fruta:
    """Representa uma fruta registada no estoque.

    :param id_fruta: ID numérico único da fruta.
    :type id_fruta: int
    :param tipo: Nome da fruta (ex: Maçã, Laranja).
    :type tipo: str
    :param especie: Variedade da fruta (ex: Gala, Fuji).
    :type especie: str
    :param peso: Quantidade em estoque (kg).
    :type peso: float
    """

def __init__(self, id_fruta, tipo, especie, peso):
        self.id = id_fruta
        self.tipo = tipo
        self.especie = especie
        self.peso = peso


class GestorFrutasBase:

    """Esta classe mostra a grelha de frutas quando o programa é executado e é a primeira coisa que o
    utilizador ver.

    Quando uma fruta é criada, esta recebe um ID para a identificar 

    :param frutas: É a lista que guarda as frutas
    :type frutas: list
    :param proximo_id: É o organizador de IDs em que a primeira fruta começa com o ID 1 
    :type proximo_id: int

    """

    def __init__(self):
        self.frutas = {}
        self.proximo_id = 1
    
    def mostrar_grelha(self):
        
        """Esta função faz construção real da grelha de frutas 
        e pocisionamento de cada atributo da fruta, onde mostra o ID, tipo, espécie e peso da fruta.

        .. note::
            Se não houver nenhuma fruta registada no stock mostra uma 
            mensagem de aviso 

        :return: A grelha
        :rtype: strings, floats e inteiros
        """


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

        """Esta função adiciona as frutas com os seus atributos 
        Primeiro se insere o tipo, de seguida a espécie e peso
        
        .. warning::
            O peso não pode ser e inferior e igual a zero

        :return: fruta e ID 
        :rtype: string e inteiro
        """


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
        """Esta função faz que o utilizador possa consultar 
           a fruta inserida recentemente atraves do ID inserido 
        .. note::
            Se não houver nenhuma fruta registada no stock e id invalido mostra uma 
            mensagem de aviso 

        :return: ID, tipo, espécie e peso 
        :rtype: strings, floats e inteiros
        """

           
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
        """Esta função atualiza os atributos de uma fruta existente atraves da inserção do ID 
        
        .. warning::
                Vai aparecer um sinal de aviso caso for pressionar "Enter" 
                se o campo ainda estiver vazio e se o id for inválido

        :return: ID, tipo, espécie e peso atualizados
        :rtype: strings, floats e inteiro
        """

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


class Cliente:
    def __init__(self, nome, morada, telefone, cidade):
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.cidade = cidade

class GestorFrutasCompleto(GestorFrutasBase):
    def fazer_pedido(self):
        print("\n--- FAZER PEDIDO (COMPRA POR PESO) ---")
        if not self.frutas:
            print("Não há frutas no estoque para venda.")
            return
        try:
            f_id = int(input("Digita o ID da fruta que o cliente quer comprar: "))
        except ValueError:
            print("ID inválido.")
            return
        fruta = self.frutas.get(f_id)
        if not fruta:
            print(f"Fruta com o ID {f_id} não existe no estoque.")
            return
        if fruta.peso <= 0:
            print(f"A fruta '{fruta.tipo}' está esgotada!")
            return
        print(f"Fruta escolhida: {fruta.tipo} ({fruta.especie})")
        print(f"Estoque disponível: {fruta.peso:.2f} kg")
        while True:
            try:
                peso_compra = float(input("\nQuantos quilos o cliente vai comprar? "))
                if peso_compra <= 0:
                    print("O peso deve ser maior que zero.")
                    continue
                if peso_compra > fruta.peso:
                    print(f"Estoque insuficiente! Apenas temos {fruta.peso:.2f} kg disponíveis.")
                    continue
                break
            except ValueError:
                print("Por favor, introduz um número válido.")

        print("\n-- DADOS DO CLIENTE --")
        nome = input("Nome: ").strip()
        morada = input("Morada: ").strip()
        telefone = input("Telefone: ").strip()
        cidade = input("Cidade: ").strip()
        
        cliente = Cliente(nome, morada, telefone, cidade)
        fruta.peso -= peso_compra
        
        print("\n" + "=" * 45)
        print(" PEDIDO CONCLUÍDO COM SUCESSO! ")
        print("=" * 45)
        print(f"Cliente: {cliente.nome}\nTelefone: {cliente.telefone}")
        print(f"Morada/Cidade: {cliente.morada}, {cliente.cidade}")
        print(f"Fruta: {fruta.tipo} ({fruta.especie})\nPeso Comprado: {peso_compra:.2f} kg\nNovo Estoque: {fruta.peso:.2f} kg")
        print("=" * 45)

    def iniciar(self):
        while True:
            self.mostrar_grelha()
            print("1. Adicionar Fruta ao Estoque\n2. Ver Fruta (por ID)\n3. Atualizar Fruta\n4. Apagar Fruta\n5. Fazer Pedido (Venda ao Cliente)\n0. Sair")
            opcao = input("\nEscolhe uma opção: ").strip()
            if opcao == "1": self.adicionar_fruta()
            elif opcao == "2": self.ver_fruta()
            elif opcao == "3": self.atualizar_fruta()
            elif opcao == "4": self.apagar_fruta()
            elif opcao == "5": self.fazer_pedido()
            elif opcao == "0":
                print("\nA encerrar o gestor... Até logo!")
                break
            else:
                print("Opção inválida! Tenta novamente.")
            input("\nPressiona ENTER para continuar...")

if __name__ == "__main__":
    gestor = GestorFrutasCompleto()
    gestor.iniciar()