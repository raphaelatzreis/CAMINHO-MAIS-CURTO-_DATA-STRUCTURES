<<<<<<< HEAD
# grafo.py - Classe responsável pela representação estruturada do grafo do sistema de transporte da EPT.

class Grafo:  # Define a classe Grafo para modelar os bairros, as rotas e as conexões de ônibus.
    def __init__(self):  # Método construtor executado automaticamente ao instanciar a classe.
        # Define um dicionário de adjacência 'self.dados' contendo a estrutura da rede de transporte.
        # A chave de primeiro nível representa o bairro de ORIGEM.
        # A chave de segundo nível representa o bairro de DESTINO.
        # O valor é uma lista de dicionários contendo tempo em minutos ("tempo") e identificador de linha ("linha").
        self.dados = {
            "Maricá": {  # Define o bairro "Maricá" como ponto de origem.
                "Flamengo": [  # Conexão direta com destino para o Flamengo.
                    {"tempo": 10, "linha": "30"},  # Ônibus linha 30 leva 10 minutos de Maricá para Flamengo.
                    {"tempo": 10, "linha": "30E"},  # Ônibus linha 30E leva 10 minutos de Maricá para Flamengo.
                    {"tempo": 10, "linha": "16"},  # Ônibus linha 16 leva 10 minutos de Maricá para Flamengo.
                    {"tempo": 10, "linha": "24"},  # Ônibus linha 24 leva 10 minutos de Maricá para Flamengo.
                ],  # Fim do grupo de conexões de Maricá para Flamengo.
                "Avenida": [  # Conexão direta com destino para Avenida.
                    {"tempo": 23, "linha": "30A"},  # Ônibus linha 30A leva 23 minutos de Maricá para Avenida.
                    {"tempo": 20, "linha": "24A"},  # Ônibus linha 24A leva 20 minutos de Maricá para Avenida.
                ]  # Fim do grupo de conexões de Maricá para Avenida.
            },  # Fim das conexões que partem de Maricá.
            
            "Flamengo": {  # Define o bairro "Flamengo" como ponto de origem.
                "Maricá": [  # Conexão direta com destino de volta para Maricá.
                    {"tempo": 10, "linha": "30"},  # Ônibus linha 30 leva 10 minutos de Flamengo para Maricá.
                    {"tempo": 10, "linha": "30E"},  # Ônibus linha 30E leva 10 minutos de Flamengo para Maricá.
                    {"tempo": 10, "linha": "16"},  # Ônibus linha 16 leva 10 minutos de Flamengo para Maricá.
                    {"tempo": 20, "linha": "24"},  # Ônibus linha 24 leva 20 minutos de Flamengo para Maricá.
                ],  # Fim do grupo de conexões de Flamengo para Maricá.
                "Parque Nanci": [  # Conexão direta com destino para Parque Nanci.
                    {"tempo": 20, "linha": "30"},  # Ônibus linha 30 leva 20 minutos de Flamengo para Parque Nanci.
                    {"tempo": 15, "linha": "30E"},  # Ônibus linha 30E leva 15 minutos de Flamengo para Parque Nanci.
                    {"tempo": 20, "linha": "16"},  # Ônibus linha 16 leva 20 minutos de Flamengo para Parque Nanci.
                    {"tempo": 20, "linha": "24"},  # Ônibus linha 24 leva 20 minutos de Flamengo para Parque Nanci.
                ]  # Fim do grupo de conexões de Flamengo para Parque Nanci.
            },  # Fim das conexões que partem de Flamengo.
            
            "Avenida": {  # Define o bairro "Avenida" como ponto de origem.
                "Maricá": [  # Conexão direta com destino de volta para Maricá.
                    {"tempo": 23, "linha": "30A"},  # Ônibus linha 30A leva 23 minutos de Avenida para Maricá.
                    {"tempo": 20, "linha": "24A"},  # Ônibus linha 24A leva 20 minutos de Avenida para Maricá.
                ],  # Fim do grupo de conexões de Avenida para Maricá.
                "Parque Nanci": [  # Conexão direta com destino para Parque Nanci.
                    {"tempo": 15, "linha": "30A"},  # Ônibus linha 30A leva 15 minutos de Avenida para Parque Nanci.
                    {"tempo": 15, "linha": "24A"},  # Ônibus linha 24A leva 15 minutos de Avenida para Parque Nanci.
                ]  # Fim do grupo de conexões de Avenida para Parque Nanci.
            },  # Fim das conexões que partem de Avenida.
            
            "Parque Nanci": {  # Define o bairro "Parque Nanci" como ponto de origem.
                "Flamengo": [  # Conexão direta com destino para Flamengo.
                    {"tempo": 20, "linha": "30"},  # Ônibus linha 30 leva 20 minutos de Parque Nanci para Flamengo.
                    {"tempo": 15, "linha": "30E"},  # Ônibus linha 30E leva 15 minutos de Parque Nanci para Flamengo.
                    {"tempo": 20, "linha": "16"},  # Ônibus linha 16 leva 20 minutos de Parque Nanci para Flamengo.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos de Parque Nanci para Flamengo.
                ],  # Fim do grupo de conexões de Parque Nanci para Flamengo.
                "Avenida": [  # Conexão direta com destino para Avenida.
                    {"tempo": 15, "linha": "30A"},  # Ônibus linha 30A leva 15 minutos de Parque Nanci para Avenida.
                    {"tempo": 5, "linha": "24A"},  # Ônibus linha 24A leva 5 minutos de Parque Nanci para Avenida.
                ],  # Fim do grupo de conexões de Parque Nanci para Avenida.
                "São José": [  # Conexão direta com destino para São José.
                    {"tempo": 10, "linha": "30"},  # Ônibus linha 30 leva 10 minutos de Parque Nanci para São José.
                    {"tempo": 10, "linha": "30A"},  # Ônibus linha 30A leva 10 minutos de Parque Nanci para São José.
                    {"tempo": 2, "linha": "16"},  # Ônibus linha 16 leva 2 minutos de Parque Nanci para São José (Conforme alteração rápida).
                    {"tempo": 5, "linha": "24A"},  # Ônibus linha 24A leva 5 minutos de Parque Nanci para São José.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos de Parque Nanci para São José.
                ],  # Fim do grupo de conexões de Parque Nanci para São José.
                "Inoã": [  # Conexão direta com destino para Inoã.
                    {"tempo": 10, "linha": "30E"}  # Ônibus linha 30E leva 10 minutos de Parque Nanci para Inoã.
                ]  # Fim do grupo de conexões de Parque Nanci para Inoã.
            },  # Fim das conexões que partem de Parque Nanci.
            
            "São José": {  # Define o bairro "São José" como ponto de origem.
                "Parque Nanci": [  # Conexão direta com destino de volta para Parque Nanci.
                    {"tempo": 10, "linha": "30"},  # Ônibus linha 30 leva 10 minutos de São José para Parque Nanci.
                    {"tempo": 10, "linha": "30A"},  # Ônibus linha 30A leva 10 minutos de São José para Parque Nanci.
                    {"tempo": 2, "linha": "16"},  # Ônibus linha 16 leva 2 minutos de São José para Parque Nanci.
                    {"tempo": 5, "linha": "24A"},  # Ônibus linha 24A leva 5 minutos de São José para Parque Nanci.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos de São José para Parque Nanci.
                ],  # Fim do grupo de conexões de São José para Parque Nanci.
                "Inoã": [  # Conexão direta com destino para Inoã.
                    {"tempo": 5, "linha": "30"},  # Ônibus linha 30 leva 5 minutos de São José para Inoã.
                    {"tempo": 5, "linha": "30A"},  # Ônibus linha 30A leva 5 minutos de São José para Inoã.
                    {"tempo": 5, "linha": "24A"},  # Ônibus linha 24A leva 5 minutos de São José para Inoã.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos de São José para Inoã.
                ]  # Fim do grupo de conexões de São José para Inoã.
            },  # Fim das conexões que partem de São José.
            
            "Inoã": {  # Define o bairro "Inoã" como ponto de origem.
                "Parque Nanci": [  # Conexão direta com destino de volta para Parque Nanci.
                    {"tempo": 10, "linha": "30E"}  # Ônibus linha 30E leva 10 minutos de Inoã para Parque Nanci.
                ],  # Fim do grupo de conexões de Inoã para Parque Nanci.
                "São José": [  # Conexão direta com destino para São José.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos de Inoã para São José.
                    {"tempo": 5, "linha": "24"},  # Ônibus linha 24 leva 5 minutos duplicado de Inoã para São José.
                    {"tempo": 5, "linha": "30"},  # Ônibus linha 30 leva 5 minutos de Inoã para São José.
                    {"tempo": 5, "linha": "30A"}  # Ônibus linha 30A leva 5 minutos de Inoã para São José.
                ],  # Fim do grupo de conexões de Inoã para São José.
                "Itaipuaçu": [  # Conexão direta com destino para Itaipuaçu.
                    {"tempo": 15, "linha": "30"},  # Ônibus linha 30 leva 15 minutos de Inoã para Itaipuaçu.
                    {"tempo": 15, "linha": "30A"},  # Ônibus linha 30A leva 15 minutos de Inoã para Itaipuaçu.
                    {"tempo": 10, "linha": "30E"}  # Ônibus linha 30E leva 10 minutos de Inoã para Itaipuaçu.
                ],  # Fim do grupo de conexões de Inoã para Itaipuaçu.
                "Recanto": [  # Conexão direta com destino para o Recanto.
                    {"tempo": 15, "linha": "21"}  # Ônibus linha 21 leva 15 minutos de Inoã para Recanto.
                ]  # Fim do grupo de conexões de Inoã para Recanto.
            },  # Fim das conexões que partem de Inoã.
            
            "Itaipuaçu": {  # Define o bairro "Itaipuaçu" como ponto de origem.
                "Inoã": [  # Conexão direta com destino de volta para Inoã.
                    {"tempo": 15, "linha": "30"},  # Ônibus linha 30 leva 15 minutos de Itaipuaçu para Inoã.
                    {"tempo": 15, "linha": "30A"},  # Ônibus linha 30A leva 15 minutos de Itaipuaçu para Inoã.
                    {"tempo": 10, "linha": "30E"}  # Ônibus linha 30E leva 10 minutos de Itaipuaçu para Inoã.
                ],  # Fim do grupo de conexões de Itaipuaçu para Inoã.
                "Recanto": [  # Conexão direta com destino para o Recanto.
                    {"tempo": 5, "linha": "30"},  # Ônibus linha 30 leva 5 minutos de Itaipuaçu para Recanto.
                    {"tempo": 5, "linha": "30A"},  # Ônibus linha 30A leva 5 minutos de Itaipuaçu para Recanto.
                    {"tempo": 2, "linha": "30E"}  # Ônibus linha 30E leva 2 minutos de Itaipuaçu para Recanto.
                ]  # Fim do grupo de conexões de Itaipuaçu para Recanto.
            },  # Fim das conexões que partem de Itaipuaçu.
            
            "Recanto": {  # Define o bairro "Recanto" como ponto de origem.
                "Itaipuaçu": [  # Conexão direta com destino de volta para Itaipuaçu.
                    {"tempo": 5, "linha": "30"},  # Ônibus linha 30 leva 5 minutos de Recanto para Itaipuaçu.
                    {"tempo": 5, "linha": "30A"},  # Ônibus linha 30A leva 5 minutos de Recanto para Itaipuaçu.
                    {"tempo": 2, "linha": "30E"}  # Ônibus linha 30E leva 2 minutos de Recanto para Itaipuaçu.
                ],  # Fim do grupo de conexões de Recanto para Itaipuaçu.
                "Inoã": [  # Conexão direta com destino de volta para Inoã.
                    {"tempo": 15, "linha": "21"}  # Ônibus linha 21 leva 15 minutos de Recanto para Inoã.
                ]  # Fim do grupo de conexões de Recanto para Inoã.
            }  # Fim das conexões que partem de Recanto.
        }  # Fim do dicionário self.dados.

    def obter_todas_linhas(self):  # Define um método para extrair todos os nomes de linhas contidos no grafo.
        linhas = set()  # Inicializa um conjunto vazio (set) para evitar linhas duplicadas.
        for u in self.dados:  # Itera sobre cada bairro de origem no dicionário.
            for v in self.dados[u]:  # Itera sobre cada bairro de destino conectado àquela origem.
                for opcao in self.dados[u][v]:  # Itera sobre cada ônibus/conexão disponível entre u e v.
                    linhas.add(opcao["linha"])  # Adiciona a linha de ônibus ao conjunto.
        return linhas  # Retorna o conjunto completo de todas as linhas únicas do sistema.
=======
# grafo.py
class Grafo:
    def __init__(self):
        # Malha viária expandida para criar múltiplas rotas de caminho mais curto
        self.dados = {
            "Flamengo": {
                "Maricá": {"tempo": 7, "linha": "E30 / E24"},
                "Parque Nanci": {"tempo": 15, "linha": "Interbairros"}
            },
            "Maricá": {
                "Flamengo": {"tempo": 7, "linha": "E30 / E24"},
                "Parque Nanci": {"tempo": 12, "linha": "E30"},
                "São José": {"tempo": 15, "linha": "Expresso / E24"},
                "Inoã": {"tempo": 35, "linha": "E11"}
            },
            "Parque Nanci": {
                "Maricá": {"tempo": 12, "linha": "E30"},
                "Flamengo": {"tempo": 15, "linha": "Interbairros"},
                "São José": {"tempo": 15, "linha": "E30"},
                "Itaipuaçu": {"tempo": 35, "linha": "E32"}
            },
            "São José": {
                "Maricá": {"tempo": 15, "linha": "Expresso / E24"},
                "Parque Nanci": {"tempo": 15, "linha": "E30"},
                "Inoã": {"tempo": 14, "linha": "E30"},
                "Recanto": {"tempo": 20, "linha": "Expresso"},
                "Itaipuaçu": {"tempo": 25, "linha": "E20"}
            },
            "Inoã": {
                "Maricá": {"tempo": 35, "linha": "E11"},
                "São José": {"tempo": 14, "linha": "E30"},
                "Itaipuaçu": {"tempo": 12, "linha": "E30"},
                "Recanto": {"tempo": 25, "linha": "E21"}
            },
            "Itaipuaçu": {
                "Inoã": {"tempo": 12, "linha": "E30"},
                "São José": {"tempo": 25, "linha": "E20"},
                "Parque Nanci": {"tempo": 35, "linha": "E32"},
                "Recanto": {"tempo": 20, "linha": "E30"}
            },
            "Recanto": {
                "Itaipuaçu": {"tempo": 20, "linha": "E30"},
                "Inoã": {"tempo": 25, "linha": "E21"},
                "São José": {"tempo": 20, "linha": "Expresso"}
            }
        }

    def obter_todas_linhas(self):
        linhas = set()
        for u in self.dados:
            for v in self.dados[u]:
                linhas.add(self.dados[u][v]["linha"])
        return linhas
>>>>>>> e58c33f0b183612affa8a0ff28276059cb07354b
