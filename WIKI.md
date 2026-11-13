# :apple: Wiki do projeto: Sistema de Gestão de Frutas

Bem vindo a documentação oficial do projeto **Gestor de frutas**.Esta wiki tem como objetivo na apresentação das ideias e práticas no desenvolvimento do software. 

---

## :dart: 1. O que é o projeto ?
O ***Sistema de Gestão de frutas*** é uma aplicação desenvolvida em python executada em linhas de comandos (CLI).Criado para simular a gestão de um empresa fornecedora alimenticia , que distribui frutas para estabelecimentos e clientes.

### Objetivos:
- Manter o controlo de stock de fruta por peso (kg).
- Utilizaçãp de operações CRUD como (Adicionar, Consultar, Atualizar, e Apagar frutas).
- Realizar a venda com a recolha de dados do cliente e atualização instantânea do stock

---

## :file_folder: 2. Estrutura de ficheiros
O repositório é constitído desta forma:

```text
gestorFrutas/
|
|__gestor_frutas.py  # Ficheiro principal com todas as classes e lógica do programa
|__.gitignore        # Ignora cache de Python (__pycache__/) e pastas do VS Code
|__README.md         #Apresentação rápida do repositório
```

---

## :building_construction: 3. Arquitetura e Estruturas de Dados

### 3.1. Paradigma Utilizado
O projeto foi criado com base sob o paradigma de **Programação Orientada a Objetos (POO)**.

### 3.2. Classes Principais:
1. **`Fruta`**:
   - `id`: Identificador numérico único.
   - `tipo`: Nome da fruta.
   - `especie`: Variedade específica.
   - `peso`: Quantidade disponível.

2. **`Cliente`**:
   - `nome`: Nome completo do cliente.
   - `morada`: Rua/Morada de entrega.
   - `telefone`: Contacto telefónico.
   - `cidade`: Cidade de residência.

3. **`GestorFrutasBase` / `GestorFrutas`**:
   - Gere o ciclo de vida do programa, validações de inserções por parte do utilizador e o menu interativo.

### 3.3. Base de Dados:
> **Nota:** Nesta fase inicial do projeto não é utilizada uma base de dados externa como MYsql, os dados são volateis , em que consiste quando o programa fechar e abrir novamente os dados são perdidos .
>
> Ainda está á ser pensado como será desenvolvido.

---
## :desktop_computer: 4. Interface do Utlizador

### Menu Princiapal

```text
============================================================
          ESTOQUE DISPONÍVEL (GRELHA DE FRUTAS)         
============================================================
ID     | Tipo            | Espécie         | Peso Disp. (kg)
------------------------------------------------------------
1      | Maçã            | Gala            | 500          
2      | Laranja         | Algarve         | 700   
============================================================

1. Adicionar Fruta ao Estoque
2. Ver Fruta (por ID)
3. Atualizar Fruta
4. Apagar Fruta
5. Fazer Pedido (Venda ao Cliente)
0. Sair

Escolhe uma opção: _

```
---

## ⚖️ 5. Regras do Gestor e Validações
- **IDs Automáticos:** O sistema gera IDs sequenciais incrementais (`proximo_id += 1`).
- **Validação de Peso:** Não são aceites valores de peso negativos ou texto inválido.
- **Venda / Pedido:** 
  - Não é possível comprar fruta com peso indisponível ou esgotada ($peso \le 0$).
  - O sistema impede compras com peso superior ao disponível em estoque.
  - No fim da compra, o peso adquirido é automaticamente subtraído ao estoque.

---

## :hammer_and_wrench: 6. Guia Git para a Equipa (Cheat-Sheet)

Para manter o repositório sincronizado e evitar conflitos de código entre os colegas, se faz os seguintes passos:

### Clonar o Repositório:
```bash
git clone https://github.com/a94091/gestorFrutas.git
cd gestorFrutas
```

### Antes de começar a programar :
Descarregar alterações dos colegas:
```bash
git pull
```

### Guardar e publicar alterações:
```bash
# 1. Verificar o que foi alterado
git status

# 2. Adicionar os ficheiros modificados
git add .

# 3. Fazer o commit com mensagem do commit
git commit -m "commit 0: descricao da funcionalidade"

# 4. Enviar para o GitHub
git push ou git push origin main
```

---

## :busts_in_silhouette: 7. Divisão de Trabalho
- **Artur:** classe `Fruta`, grelha de frutas com as suas caracteristicas e operações CRUD de estoque.
- **Pessoa 2:** Criação da classe `Cliente`, implementação do fluxo de pedidos/vendas e ciclo do menu interativo da aplicação.


