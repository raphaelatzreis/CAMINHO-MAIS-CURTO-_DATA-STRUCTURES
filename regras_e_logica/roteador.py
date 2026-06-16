# roteador.py - Classe responsável pela lógica de roteamento e busca do caminho mínimo utilizando o algoritmo de Dijkstra.

import heapq  # Importa a biblioteca heapq para gerenciar a fila de prioridades (min-heap) eficiente.

class Roteador:  # Define a classe Roteador para encapsular as regras de cálculo de rotas.
    def __init__(self, grafo_obj):  # Construtor da classe que recebe o objeto Grafo via injeção de dependência.
        # Armazena o objeto grafo injetado para poder acessar a estrutura de dados das linhas e tempos de viagem.
        self.grafo_obj = grafo_obj  
        # Inicializa um conjunto (set) para registrar as linhas de ônibus que foram desativadas temporariamente.
        self.linhas_desativadas = set()  

    def calcular_caminho(self, inicio, fim):  # Método que executa Dijkstra para encontrar o menor tempo de percurso de inicio até fim.
        # Cria a fila de prioridades contendo tuplas de: (tempo_acumulado, nó_atual, caminho_percorrido, linhas_usadas).
        fila = [(0, inicio, [inicio], [])]  
        # Inicializa um dicionário de visitados para rastrear o menor tempo gasto para alcançar cada bairro.
        visitados = {}  
        
        while fila:  # Loop principal executado enquanto existirem caminhos a processar na fila de prioridades.
            # Remove e retorna o estado com o menor tempo acumulado atual da fila de prioridade (min-heap).
            tempo, atual, caminho, linhas = heapq.heappop(fila)  
            
            if atual == fim:  # Caso o nó atual retirado da fila seja o destino final solicitado:
                # Retorna o tempo total acumulado, a lista ordenada do caminho e as linhas de ônibus correspondentes utilizadas.
                return tempo, caminho, list(linhas)  
                
            # Se o nó atual já foi visitado com um tempo igual ou menor ao acumulado atual, ignora este ramo (otimização).
            if atual in visitados and visitados[atual] <= tempo:  
                continue  # Pula o restante do processamento deste nó e passa para a próxima iteração.
            # Registra o menor tempo de chegada encontrado até o momento para o nó atual.
            visitados[atual] = tempo  
            
            # Obtém os vizinhos conectados diretamente ao bairro atual a partir do dicionário de dados do grafo.
            vizinhos = self.grafo_obj.dados.get(atual, {})  
            for vizinho, opcoes in vizinhos.items():  # Itera sobre cada bairro vizinho e suas respectivas opções de ônibus.
                for opcao in opcoes:  # Itera sobre cada ônibus (opção de linha e tempo de viagem) conectado a esse vizinho.
                    linha = opcao["linha"]  # Extrai o nome da linha de ônibus da opção.
                    
                    # Se a linha de ônibus estiver no conjunto de linhas desativadas, ignora a opção e não calcula o trajeto por ela.
                    if linha in self.linhas_desativadas:  
                        continue  # Ignora este ônibus e pula para a próxima opção.
                        
                    tempo_aresta = opcao["tempo"]  # Extrai o tempo de percurso necessário para percorrer essa aresta.
                    # Insere o novo estado na fila de prioridades acumulando o tempo da viagem, salvando o caminho e a linha utilizada.
                    heapq.heappush(fila, (tempo + tempo_aresta, vizinho, caminho + [vizinho], linhas + [linha]))  
                    
        return None, [], []  # Caso a fila esvazie sem encontrar o destino, retorna valores padrão representando erro/sem rota.


    def alternar_linha(self, linha):  # Método responsável por ativar ou desativar uma linha de ônibus.
        if linha in self.linhas_desativadas:  # Se a linha de ônibus já estiver listada no conjunto de desativadas:
            self.linhas_desativadas.remove(linha)  # Remove a linha do conjunto, reativando-a para futuros cálculos de rotas.
            return True  # Retorna True indicando que a linha agora está ATIVA e operando.
        else:  # Caso contrário (se a linha estiver ativa atualmente):
            self.linhas_desativadas.add(linha)  # Adiciona a linha ao conjunto de desativadas, bloqueando-a em novos trajetos.
            return False  # Retorna False indicando que a linha foi DESATIVADA e posta fora de serviço.