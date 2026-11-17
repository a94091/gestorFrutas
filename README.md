#  Sistema de Gestão de Frutas e Vendas

Aplicação de linha de comandos feita em Python para gerir o inventário de frutas e processar pedidos de venda ao cliente.

## Funcionalidades do programa

* **Visualização de Stock:** Mostra uma tabela com o ID, tipo, espécie e peso disponível de todas as frutas.
* **Consultar Fruta:** Permite pesquisar os detalhes de uma fruta através do seu ID.
* **Atualizar Fruta:** Altera os dados (tipo, espécie e peso) de uma fruta que ja existe.
* **Adicionar Fruta:** Regista novas frutas no stock.
* **Apagar Fruta:** Pode-se apagar uma fruta especificando o ID da fruta.
* **Fazer Pedido (Venda):**
  * Verifica a disponibilidade e o peso em stock.
  * Recolhe os dados do cliente (nome, morada, telefone e cidade).
  * Tira automaticamente o peso comprado ao stock disponível e mostra um resumo do pedido.

## Como Executar

### Pré-requisitos
* **Python** instalado no sistema.

### Como iniciar o programa
1. Guarda o código `gestor_frutas.py` numa pasta.
2. Abre a linha de comandos na pasta onde guardaste o ficheiro.
3. Executa o seguinte comando:

```bash
python gestor_frutas.py
```

