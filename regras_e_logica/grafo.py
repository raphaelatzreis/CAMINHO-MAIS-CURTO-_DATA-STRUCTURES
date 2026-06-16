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
