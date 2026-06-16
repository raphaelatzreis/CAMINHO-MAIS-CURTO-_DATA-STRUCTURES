# Sistema de Simulação de Rotas EPT com Algoritmo de Dijkstra

Projeto desenvolvido para a disciplina de Estruturas de Dados com o objetivo de modelar a rede de transporte da Empresa Pública de Transportes (EPT) de Maricá utilizando Grafos e o Algoritmo de Dijkstra para determinação de rotas de menor custo.

## Sobre o Projeto

O sistema representa bairros e terminais da cidade de Maricá como vértices de um grafo ponderado. As conexões entre eles representam linhas de ônibus, contendo informações sobre tempo estimado de deslocamento e identificação da linha.

A aplicação permite que o usuário selecione um ponto de origem e um ponto de destino para que o algoritmo calcule automaticamente a rota mais rápida disponível.

Além disso, é possível simular a indisponibilidade de determinadas linhas, permitindo analisar como alterações na malha de transporte impactam os caminhos encontrados.

## Funcionalidades

* Cálculo de rotas utilizando o algoritmo de Dijkstra;
* Determinação do menor tempo de deslocamento entre dois pontos;
* Exibição das linhas utilizadas durante o trajeto;
* Simulação de linhas temporariamente fora de serviço;
* Reativação de linhas previamente desativadas;
* Visualização gráfica da rede de transporte;
* Destaque visual do caminho encontrado.

## Conceitos Aplicados

### Estruturas de Dados

* Grafos
* Dicionários
* Listas
* Conjuntos (Set)
* Filas de Prioridade (Heap)

### Algoritmos

* Algoritmo de Dijkstra
* Busca de Caminho Mínimo
* Estratégia Gulosa (Greedy)

### Programação

* Programação Orientada a Objetos
* Injeção de Dependência
* Separação de Responsabilidades

## Estrutura do Projeto

```text
📦 Projeto
│
├── main.py
│
├── regras_e_logica
│   ├── grafo.py
│   └── roteador.py
│
└── ui_interface_usuario
    └── interface.py
```

### main.py

Responsável pela inicialização da aplicação e integração dos componentes do sistema.

### grafo.py

Armazena a estrutura da rede de transporte, incluindo bairros, conexões, tempos de deslocamento e identificação das linhas.

### roteador.py

Implementa o algoritmo de Dijkstra e realiza o processamento das rotas, considerando também linhas desativadas.

### interface.py

Responsável pela interface gráfica, entrada de dados do usuário e visualização da rede através das bibliotecas Matplotlib e NetworkX.

## Regiões Representadas

A simulação contempla os seguintes pontos da cidade de Maricá:

* Terminal Centro
* Inoã
* Itaipuaçu
* São José
* Araçatiba
* Jacaroá
* Retiro
* Espraiado
* Guaratiba
* Maricá
* Ponta Negra
* Jaconé
* Cordeirinho
* Recanto
* Cajueiros

## Tecnologias Utilizadas

* Python 3
* Matplotlib
* NetworkX
* Heapq

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/raphaelatzreis/CAMINHO-MAIS-CURTO-_DATA-STRUCTURES.git
```

Acesse a pasta do projeto:

```bash
cd CAMINHO-MAIS-CURTO-_DATA-STRUCTURES
```

Instale as dependências:

```bash
pip install matplotlib networkx
```

Execute a aplicação:

```bash
python main.py
```

## Exemplo de Uso

1. Informar o ponto de partida.
2. Informar o destino desejado.
3. Solicitar o cálculo da rota.
4. Visualizar o trajeto encontrado, o tempo total e as linhas utilizadas.

Também é possível informar o código de uma linha para simular sua interrupção e verificar como o sistema recalcula caminhos alternativos.

## Diferenciais do Projeto

* Implementação própria do algoritmo de Dijkstra utilizando fila de prioridade (`heapq`);
* Representação da malha de transporte da EPT de Maricá;
* Simulação de interrupção de linhas de ônibus;
* Visualização gráfica das conexões entre bairros;
* Arquitetura orientada a objetos com separação entre dados, processamento e interface.

## Fundamentação Teórica

O algoritmo de Dijkstra foi desenvolvido pelo cientista da computação Edsger W. Dijkstra em 1956 e é amplamente utilizado para resolução de problemas de caminho mínimo em grafos ponderados.

Aplicações desse algoritmo podem ser encontradas em sistemas de navegação GPS, roteamento de redes de computadores, logística e planejamento de transportes.

## Autores

Raphaela Zille

Marcos Gabriel Sales Pires

Ravi Carlos Diano

Matheus Duarte 





