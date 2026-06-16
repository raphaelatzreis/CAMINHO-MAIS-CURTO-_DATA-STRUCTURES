import unicodedata
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import networkx as nx


class InterfaceEPT:
    def __init__(self, roteador):
        self.roteador = roteador

        self.fig, self.ax_main = plt.subplots(figsize=(10, 8), facecolor="#F4F6F9")
        plt.subplots_adjust(bottom=0.35, top=0.85, left=0.05, right=0.95)

        self.ax_log = plt.axes([0.65, 0.10, 0.30, 0.20], facecolor="#FFFFFF")
        self.ax_log.axis("off")

        self.configurar_widgets()
        self.atualizar_plot()
        self.atualizar_log("Olá! Bem-vindo ao sistema de rotas.\n\nDigite origem e destino para calcular a rota.")

    def normalizar_texto(self, texto):
        texto = texto.strip().lower()
        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
        return texto

    def encontrar_nome_real(self, texto_digitado):
        texto_normalizado = self.normalizar_texto(texto_digitado)

        for parada in self.roteador.grafo_obj.dados.keys():
            if self.normalizar_texto(parada) == texto_normalizado:
                return parada

        return None

    def obter_dados_aresta(self, u, v):
        dados_grafo = self.roteador.grafo_obj.dados

        if u in dados_grafo and v in dados_grafo[u]:
            return dados_grafo[u][v]

        if v in dados_grafo and u in dados_grafo[v]:
            return dados_grafo[v][u]

        return None

    def atualizar_log(self, texto):
        self.ax_log.clear()
        self.ax_log.axis("off")
        self.ax_log.text(
            0.05,
            0.95,
            "DETALHES DA OPERAÇÃO:",
            fontsize=10,
            fontweight="bold",
            color="#E30613",
            va="top"
        )
        self.ax_log.text(
            0.05,
            0.75,
            texto,
            fontsize=9.5,
            color="#333333",
            va="top"
        )
        self.fig.canvas.draw_idle()

    def atualizar_plot(self, caminho_destacado=None):
        self.ax_main.clear()
        self.ax_main.set_title(
            "MAPA DE ROTAS EPT - MARICÁ",
            fontsize=15,
            fontweight="bold",
            color="#CC0000",
            pad=20
        )

        dados_grafo = self.roteador.grafo_obj.dados
        linhas_off = self.roteador.linhas_desativadas

        G = nx.Graph()

        for origem, vizinhos in dados_grafo.items():
            for destino in vizinhos:
                G.add_edge(origem, destino)

        posicoes_base = {
            "Recanto": (-11, 2),
            "Itaipuaçu": (-11, -1),
            "Inoã": (-5, -2),
            "Maricá": (-5, 0.5),
            "São José": (0, -1),
            "Flamengo": (0, 2),
            "Parque Nanci": (4, 0.5),
            "Terminal Centro": (-2, 0),
            "Araçatiba": (-0.5, -2.5),
            "Jacaroá": (3, -1.5),
            "Retiro": (-1.5, 3.5),
            "Espraiado": (4, 3.5),
            "Cajueiros": (-7.5, -3.5),
            "Guaratiba": (4.5, -3),
            "Ponta Negra": (8, -1),
            "Cordeirinho": (7, -3.5),
            "Jaconé": (10.5, -1),
        }

        pos_fixas = {
            no: coords
            for no, coords in posicoes_base.items()
            if no in G.nodes()
        }

        if len(pos_fixas) == len(G.nodes()):
            pos = pos_fixas
        else:
            pos = nx.spring_layout(G, pos=pos_fixas, fixed=list(pos_fixas.keys()), seed=42)

        pos_labels = {
            no: (coords[0], coords[1] + 0.35)
            for no, coords in pos.items()
        }

        nx.draw_networkx_nodes(
            G,
            pos,
            ax=self.ax_main,
            node_size=600,
            node_color="#E30613",
            edgecolors="white",
            linewidths=2
        )

        nx.draw_networkx_labels(
            G,
            pos_labels,
            ax=self.ax_main,
            font_size=9,
            font_weight="bold"
        )

        edges_normais = []
        edges_desativados = []
        edges_caminho = []

        for u, v in G.edges():
            dados_aresta = self.obter_dados_aresta(u, v)

            if dados_aresta is None:
                continue

            linha = dados_aresta["linha"]

            no_caminho = False

            if caminho_destacado:
                for i in range(len(caminho_destacado) - 1):
                    atual = caminho_destacado[i]
                    proximo = caminho_destacado[i + 1]

                    if (atual == u and proximo == v) or (atual == v and proximo == u):
                        no_caminho = True
                        break

            if no_caminho:
                edges_caminho.append((u, v))
            elif linha in linhas_off:
                edges_desativados.append((u, v))
            else:
                edges_normais.append((u, v))

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges_normais,
            ax=self.ax_main,
            width=2,
            edge_color="#3498DB"
        )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges_desativados,
            ax=self.ax_main,
            width=2,
            edge_color="#7F8C8D",
            style="dashed"
        )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges_caminho,
            ax=self.ax_main,
            width=4,
            edge_color="#27AE60"
        )

        labels_arestas = {}

        for u, v in G.edges():
            dados_aresta = self.obter_dados_aresta(u, v)

            if dados_aresta is None:
                continue

            linha = dados_aresta["linha"]
            tempo = dados_aresta["tempo"]

            status = " OFF" if linha in linhas_off else ""
            labels_arestas[(u, v)] = f"{linha}\n({tempo}min){status}"

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labels_arestas,
            ax=self.ax_main,
            font_size=7,
            rotate=False,
            bbox=dict(
                boxstyle="round,pad=0.2",
                facecolor="white",
                edgecolor="none",
                alpha=0.8
            )
        )

        self.ax_main.axis("off")
        self.fig.canvas.draw_idle()

    def buscar_caminho_click(self, event):
        origem_digitada = self.box_origem.text
        destino_digitado = self.box_destino.text

        if not origem_digitada.strip() or not destino_digitado.strip():
            self.atualizar_log("[ERRO]\nPreencha os campos de origem e destino.")
            return

        origem = self.encontrar_nome_real(origem_digitada)
        destino = self.encontrar_nome_real(destino_digitado)

        if origem is None:
            self.atualizar_log(f"[ERRO]\nA parada '{origem_digitada}' não foi encontrada.")
            return

        if destino is None:
            self.atualizar_log(f"[ERRO]\nA parada '{destino_digitado}' não foi encontrada.")
            return

        tempo, caminho, linhas = self.roteador.calcular_caminho(origem, destino)

        if caminho:
            caminho_str = " → ".join(caminho)
            linhas_str = ", ".join(linhas)

            self.atualizar_log(
                f"Rota encontrada!\n\n"
                f"Trajeto:\n{caminho_str}\n\n"
                f"Tempo total: {tempo} min\n\n"
                f"Linhas usadas: {linhas_str}"
            )

            self.atualizar_plot(caminho_destacado=caminho)
        else:
            self.atualizar_log(
                "[ALERTA]\nNão existe rota ativa entre essas paradas."
            )
            self.atualizar_plot()

    def toggle_linha_click(self, event):
        linha = self.box_linha.text.strip().upper()

        if not linha:
            self.atualizar_log("[ERRO]\nDigite o número da linha.")
            return

        linhas_existentes = self.roteador.grafo_obj.obter_todas_linhas()

        if linha not in linhas_existentes:
            self.atualizar_log(f"[ERRO]\nA linha {linha} não existe.")
            return

        reativada = self.roteador.alternar_linha(linha)

        if reativada:
            self.atualizar_log(f"LINHA REATIVADA:\n\nA linha {linha} voltou a operar.")
        else:
            self.atualizar_log(f"LINHA DESATIVADA:\n\nA linha {linha} saiu de operação.")

        self.atualizar_plot()

    def configurar_widgets(self):
        self.ax_txt_origem = plt.axes([0.10, 0.25, 0.10, 0.04])
        self.box_origem = widgets.TextBox(self.ax_txt_origem, "Partida: ", initial="")

        self.ax_txt_destino = plt.axes([0.30, 0.25, 0.10, 0.04])
        self.box_destino = widgets.TextBox(self.ax_txt_destino, "Destino: ", initial="")

        self.ax_btn_buscar = plt.axes([0.42, 0.25, 0.12, 0.04])
        self.btn_buscar = widgets.Button(
            self.ax_btn_buscar,
            "Achar Rota",
            color="#27AE60",
            hovercolor="#229954"
        )
        self.btn_buscar.label.set_color("white")
        self.btn_buscar.label.set_fontweight("bold")
        self.btn_buscar.on_clicked(self.buscar_caminho_click)

        self.ax_txt_linha = plt.axes([0.10, 0.18, 0.10, 0.04])
        self.box_linha = widgets.TextBox(self.ax_txt_linha, "Linha: ", initial="")

        self.ax_btn_toggle = plt.axes([0.22, 0.18, 0.12, 0.04])
        self.btn_toggle = widgets.Button(
            self.ax_btn_toggle,
            "Alternar",
            color="#F39C12",
            hovercolor="#D68910"
        )
        self.btn_toggle.label.set_color("white")
        self.btn_toggle.label.set_fontweight("bold")
        self.btn_toggle.on_clicked(self.toggle_linha_click)

    def iniciar(self):
        plt.show()
