# interface.py - Módulo responsável pela interface gráfica do usuário (GUI) utilizando o Matplotlib e NetworkX.

import matplotlib.pyplot as plt  # Importa a biblioteca para desenhar gráficos e criar a janela gráfica da aplicação.
import matplotlib.widgets as widgets  # Importa componentes interativos de UI como TextBox e Button.
import networkx as nx  # Importa a biblioteca para modelagem e visualização do grafo da rede de transporte.

class InterfaceEPT:  # Define a classe InterfaceEPT para gerenciar e renderizar a tela da aplicação.
    def __init__(self, roteador):  # Método construtor que inicializa a interface, recebendo o Roteador.
        self.roteador = roteador  # Armazena a referência para o roteador injetado.
        
        self.texto_origem = ""  # Inicializa a variável para armazenar o texto digitado de origem da rota.
        self.texto_destino = ""  # Inicializa a variável para armazenar o texto digitado de destino da rota.
        self.texto_linha = ""  # Inicializa a variável para armazenar o número da linha a ser alternada.

        # Cria a janela principal do Matplotlib com tamanho e cor de fundo cinza claro personalizado.
        self.fig, self.ax_main = plt.subplots(figsize=(10, 8), facecolor="#F4F6F9")
        # Define as margens da janela principal deixando espaço na parte inferior para os botões e texto.
        plt.subplots_adjust(bottom=0.35, top=0.85, left=0.05, right=0.95)

        # Configura a posição do painel de log (retângulo branco para texto informativo) na parte inferior direita.
        self.ax_log = plt.axes([0.65, 0.06, 0.30, 0.24], facecolor="#FFFFFF")
        self.ax_log.axis("off")  # Desativa os eixos cartesianos no painel de log para manter apenas o fundo limpo.

        self.configurar_widgets()  # Chama o método interno para desenhar e configurar os inputs e botões na tela.
        self.atualizar_plot()  # Chama o método interno para renderizar o grafo de rotas e bairros inicial.
        # Imprime uma mensagem de boas-vindas inicial no painel de detalhes da operação.
        self.atualizar_log("Olá! Bem-vindo ao sistema de rotas.\n\nUse os controles ao lado para simular\ne gerenciar o tráfego.")

    def atualizar_log(self, texto):  # Método responsável por atualizar o conteúdo informativo do painel de log.
        self.ax_log.clear()  # Limpa o texto desenhado anteriormente para evitar sobreposição.
        self.ax_log.axis("off")  # Garante que as linhas cartesianas fiquem ocultas após a limpeza.
        
        import textwrap  # Importa a biblioteca textwrap localmente para lidar com quebra de linhas longas.
        linhas_wrapped = []  # Inicializa uma lista para armazenar as linhas já formatadas com quebra automática.
        for linha in texto.split("\n"):  # Divide a string recebida em linhas individuais.
            if linha.strip():  # Se a linha não for puramente espaços em branco:
                # Quebra a linha em múltiplos segmentos caso ultrapasse o limite de 42 caracteres.
                linhas_wrapped.append(textwrap.fill(linha, width=42))
            else:  # Caso a linha esteja vazia:
                linhas_wrapped.append("")  # Preserva a quebra de linha original.
        texto_wrapped = "\n".join(linhas_wrapped)  # Junta novamente todas as linhas formatadas usando quebras de linha.
        
        # Desenha o título do painel "DETALHES DA OPERAÇÃO:" em vermelho oficial no topo do painel.
        self.ax_log.text(0.05, 0.95, "DETALHES DA OPERAÇÃO:", fontsize=10, fontweight="bold", color="#E30613", va="top")
        # Desenha a mensagem recebida formatada e alinhada logo abaixo do título no painel.
        self.ax_log.text(0.05, 0.82, texto_wrapped, fontsize=9.5, color="#333333", va="top")
        self.fig.canvas.draw_idle()  # Solicita que a tela seja redesenhada de maneira eficiente.

    def atualizar_plot(self, caminho_destacado=None):  # Método que renderiza o mapa visual dos caminhos e bairros.
        self.ax_main.clear()  # Limpa a área de plot principal antes de redesenhar os nós e linhas do grafo.
        # Define o título principal da aplicação centralizado no topo com cor vermelha da EPT.
        self.ax_main.set_title("SISTEMA DE TRANSPORTE EPT - MARICÁ", fontsize=15, fontweight="bold", color="#CC0000", pad=20)
        
        dados_grafo = self.roteador.grafo_obj.dados  # Obtém o dicionário de rotas do roteador.
        linhas_off = self.roteador.linhas_desativadas  # Obtém o conjunto de linhas desativadas do roteador.
        
        G = nx.Graph()  # Cria um objeto de Grafo vazio na biblioteca NetworkX.
        for u in dados_grafo:  # Itera sobre cada origem de bairro no grafo.
            for v in dados_grafo[u]:  # Itera sobre cada destino direto a partir de u.
                G.add_edge(u, v)  # Adiciona uma aresta representando a rota direta entre os dois bairros no NetworkX.
                
        posicoes_base = {  # Dicionário estático com as coordenadas (x, y) reais dos bairros de Maricá.
            "Maricá": (0, 0),
            "Avenida": (1.5, 1.5),
            "Flamengo": (1.5, -1.5),
            "Parque Nanci": (3.5, 0),
            "São José": (6.0, 1.5),
            "Inoã": (11.0, 1.5),
            "Itaipuaçu": (11.0, -3.0),
            "Recanto": (13.5, -3.0)
        }  # Coordenadas estáticas mapeadas.
        
        # Filtra apenas os nós presentes no grafo atual para posicionamento no plano cartesiano.
        pos_fixas = {no: coords for no, coords in posicoes_base.items() if no in G.nodes()}
        if len(pos_fixas) == len(G.nodes()):  # Se todos os nós tiverem coordenada estática definida:
            pos = pos_fixas  # Aplica o mapeamento direto.
        else:  # Caso falte alguma coordenada:
            # Calcula posições automáticas utilizando força de mola para nós faltantes.
            pos = nx.spring_layout(G, pos=pos_fixas, fixed=pos_fixas.keys(), seed=42)
        
        pos_labels = {}  # Inicializa dicionário de posições das etiquetas de nomes dos bairros.
        for no, coords in pos.items():  # Itera sobre a posição de cada nó.
            pos_labels[no] = (coords[0], coords[1] + 0.4)  # Desloca o nome do bairro levemente para cima do nó circular.
            
        # Desenha os nós circulares (bairros) na cor vermelha característica com bordas brancas e tamanho personalizado.
        nos = nx.draw_networkx_nodes(G, pos, ax=self.ax_main, node_size=600, node_color="#E30613", edgecolors="white", linewidths=2)
        nos.set_zorder(3)  # Garante que as bolinhas dos bairros apareçam acima das linhas das arestas no desenho.
        
        # Define o estilo visual das caixas das etiquetas dos nomes dos bairros (fundo branco, borda fina).
        fundo_cidades = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#DDDDDD", alpha=0.9)
        # Renderiza os nomes dos bairros posicionados logo acima das esferas.
        labels_cidades = nx.draw_networkx_labels(G, pos_labels, ax=self.ax_main, font_size=9, font_weight="bold", font_family="sans-serif", verticalalignment="bottom", bbox=fundo_cidades)
        
        for texto in labels_cidades.values():  # Itera sobre cada componente de texto renderizado dos bairros.
            texto.set_color("#2C3E50")  # Altera a cor da fonte para um azul escuro/cinza moderno menos cansativo que o preto.
            texto.set_zorder(4)  # Garante que os nomes dos bairros fiquem acima de todos os elementos gráficos.
        
        edges_normais, edges_desativados, edges_caminho = [], [], []  # Listas para segregar tipos de conexões no desenho.
        
        for u, v in G.edges():  # Itera sobre cada aresta no grafo geral do NetworkX.
            opcoes = dados_grafo[u][v]  # Recupera todas as linhas de ônibus ligando u e v.
            todas_desativadas = all(op["linha"] in linhas_off for op in opcoes)  # Verifica se absolutamente todas as linhas dali estão desativadas.
            no_caminho = False  # Flag para rastrear se a aresta faz parte da rota em destaque buscada.
            
            if caminho_destacado:  # Se houver um caminho selecionado a ser exibido:
                for i in range(len(caminho_destacado) - 1):  # Itera sobre os nós da rota destacada sequencialmente.
                    # Verifica se o par ordenado atual u-v coincide com este passo da rota percorrida.
                    if (caminho_destacado[i] == u and caminho_destacado[i+1] == v) or (caminho_destacado[i] == v and caminho_destacado[i+1] == u):
                        no_caminho = True  # Marca a flag como verdadeira.
                        break  # Interrompe o laço de verificação.
                        
            if no_caminho:  # Se pertence ao caminho ativo calculado:
                edges_caminho.append((u, v))  # Adiciona ao grupo de arestas destacadas.
            elif todas_desativadas:  # Se todas as linhas desse trecho estão desligadas:
                edges_desativados.append((u, v))  # Adiciona ao grupo de linhas desativadas.
            else:  # Se tem ao menos uma linha operando e não faz parte da rota em destaque:
                edges_normais.append((u, v))  # Adiciona ao grupo de arestas normais.
                
        # Desenha as conexões normais com linhas contínuas em cinza claro moderno.
        linhas_n = nx.draw_networkx_edges(G, pos, edgelist=edges_normais, ax=self.ax_main, width=2, edge_color="#BDC3C7", style="solid")
        if linhas_n: linhas_n.set_zorder(1)  # Define ordem de desenho inferior para não sobrepor nós.
            
        # Desenha as conexões desativadas com linhas pontilhadas cinzas indicando fora de serviço.
        linhas_d = nx.draw_networkx_edges(G, pos, edgelist=edges_desativados, ax=self.ax_main, width=2, edge_color="#7F8C8D", style="dashed")
        if linhas_d: linhas_d.set_zorder(1)  # Define ordem de desenho inferior.
            
        # Desenha o caminho mínimo destacado com uma linha espessa na cor verde vibrante.
        if edges_caminho:  # Se a lista de arestas destacadas não estiver vazia:
            linhas_c = nx.draw_networkx_edges(G, pos, edgelist=edges_caminho, ax=self.ax_main, width=4.5, edge_color="#27AE60", style="solid")
            if linhas_c: linhas_c.set_zorder(2)  # Posiciona o destaque verde acima das conexões normais, mas abaixo dos bairros.
            
        midpoint_groups = {}  # Inicializa mapeamento para agrupar arestas que compartilham o mesmo ponto médio no plano.
        for u, v in G.edges():  # Itera sobre todas as arestas do grafo.
            pu, pv = pos[u], pos[v]  # Recupera as posições geométricas dos dois nós.
            # Calcula e arredonda o ponto médio exato da linha conectando os dois nós.
            mx, my = round((pu[0] + pv[0]) / 2, 2), round((pu[1] + pv[1]) / 2, 2)
            key = (mx, my)  # Usa as coordenadas de ponto médio como chave.
            if key not in midpoint_groups:  # Se a chave não existir no dicionário:
                midpoint_groups[key] = []  # Inicializa uma lista vazia.
            midpoint_groups[key].append((u, v))  # Adiciona a aresta ao respectivo ponto médio correspondente.
            
        # Estilo visual das caixinhas brancas onde são listadas as linhas de ônibus com tempo.
        caixa_texto = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#EEEEEE", alpha=0.9)

        for key, edges in midpoint_groups.items():  # Itera sobre os grupos de ponto médio calculados.
            if len(edges) == 1:  # Se existir apenas uma conexão nesse local físico do gráfico:
                u, v = edges[0]  # Recupera os nós.
                opcoes = dados_grafo[u][v]  # Recupera a lista de ônibus desse trecho.
                linhas_por_tempo = {}  # Agrupa as linhas pelo respectivo tempo de viagem.
                for op in opcoes:  # Itera sobre as linhas de ônibus disponíveis.
                    t = op["tempo"]  # Pega o tempo da opção.
                    l = op["linha"]  # Pega o nome da linha de ônibus.
                    status = f"{l}" + ("(OFF)" if l in linhas_off else "")  # Adiciona o aviso (OFF) se a linha estiver inativa.
                    if t not in linhas_por_tempo:  # Se o tempo não estiver mapeado:
                        linhas_por_tempo[t] = []  # Inicializa lista para aquele tempo.
                    linhas_por_tempo[t].append(status)  # Adiciona o status da linha.
                
                linhas_label = []  # Cria a lista de strings para montagem do rótulo final.
                for t, lst in linhas_por_tempo.items():  # Itera sobre os tempos e suas linhas agrupadas.
                    if len(lst) >= 2:  # Se houver mais de uma linha com o mesmo tempo:
                        # Exibe formatado como (linha1 / linha2) (Xm)
                        linhas_label.append(f"({ ' / '.join(lst) }) ({t}m)")
                    else:  # Caso seja linha única com esse tempo:
                        # Exibe formatado como linha1 (Xm)
                        linhas_label.append(f"{lst[0]} ({t}m)")
                lbl_str = "\n".join(linhas_label)  # Junta as informações do rótulo separando por quebras de linha.
                lbl = {(u, v): lbl_str}  # Mapeia o rótulo para a aresta (u, v).
                
                # Desenha o rótulo da aresta centralizado na conexão.
                nx.draw_networkx_edge_labels(G, pos, edge_labels=lbl, ax=self.ax_main, 
                font_size=7, font_color="#555555", label_pos=0.5, 
                rotate=False, bbox=caixa_texto)
            else:  # Caso existam conexões sobrepostas com caminhos paralelos:
                num_edges = len(edges)  # Armazena a contagem total de arestas sobrepostas.
                for i, (u, v) in enumerate(edges):  # Itera ordenadamente indexando cada uma delas.
                    # Calcula uma distribuição proporcional para posicionar o texto ao longo da aresta, evitando colisões.
                    pos_val = 0.3 if num_edges == 2 and i == 0 else (0.7 if num_edges == 2 else 0.2 + (0.6 * i / (num_edges - 1)))
                    opcoes = dados_grafo[u][v]  # Recupera a lista de linhas.
                    linhas_por_tempo = {}  # Agrupa linhas pelo tempo de percurso.
                    for op in opcoes:  # Itera sobre os dados.
                        t = op["tempo"]  # Extrai tempo.
                        l = op["linha"]  # Extrai nome da linha.
                        status = f"{l}" + ("(OFF)" if l in linhas_off else "")  # Adiciona aviso de desativada se necessário.
                        if t not in linhas_por_tempo:  # Se o tempo não estiver mapeado:
                            linhas_por_tempo[t] = []  # Cria a chave no dicionário.
                        linhas_por_tempo[t].append(status)  # Adiciona a linha de ônibus.
                    
                    linhas_label = []  # Lista para formatar os textos do rótulo.
                    for t, lst in linhas_por_tempo.items():  # Itera sobre os tempos agrupados.
                        if len(lst) >= 2:  # Se houver múltiplas linhas para o mesmo tempo:
                            linhas_label.append(f"({ ' / '.join(lst) }) ({t}m)")  # Agrupa entre parênteses.
                        else:  # Se for única:
                            linhas_label.append(f"{lst[0]} ({t}m)")  # Exibe diretamente.
                    lbl_str = "\n".join(linhas_label)  # Junta tudo com quebra de linha.
                    lbl = {(u, v): lbl_str}  # Associa o rótulo à aresta.
                    
                    # Desenha a caixa de texto na posição deslocada pos_val calculada.
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=lbl, ax=self.ax_main, 
                    font_size=7, font_color="#555555", label_pos=pos_val, 
                    rotate=False, bbox=caixa_texto)
        
        for text in self.ax_main.texts:  # Itera sobre todos os elementos de texto no gráfico principal.
            if text.get_zorder() == 1:  # Se o nível de ordem for igual a 1 (padrão do matplotlib para etiquetas de arestas):
                text.set_zorder(2)  # Promove para nível 2 para que os rótulos fiquem bem legíveis acima das linhas cinzas.

        self.ax_main.margins(x=0.15, y=0.25)  # Adiciona margens generosas nas laterais do gráfico para evitar cortes nas bordas.
        self.ax_main.axis("off")  # Desliga a grade cartesiana geral do gráfico de nós.
        self.fig.canvas.draw_idle()  # Atualiza os desenhos na tela eficientemente.

    def txt_origem_changed(self, val): self.texto_origem = val.strip()  # Atualiza self.texto_origem sempre que o usuário digitar na caixa de origem.
    def txt_destino_changed(self, val): self.texto_destino = val.strip()  # Atualiza self.texto_destino sempre que o usuário digitar na caixa de destino.
    def txt_linha_changed(self, val): self.texto_linha = val.strip()  # Atualiza self.texto_linha sempre que o usuário digitar na caixa da linha de ônibus.

    def buscar_caminho_click(self, event):  # Método chamado quando o usuário clica no botão "Achar Rota".
        try:  # Abre o bloco try-catch para capturar possíveis erros de bairros inexistentes.
            if not self.texto_origem or not self.texto_destino:  # Se algum dos campos de entrada estiver em branco:
                self.atualizar_log("[ERRO]\nPreencha os campos de\nOrigem e Destino!")  # Exibe aviso de erro no log.
                return  # Aborta o fluxo da função.
                
            # Converte a entrada digitada para formato Capitalizado (Ex: "recanto" -> "Recanto") para compatibilidade.
            inicio, fim = self.texto_origem.title(), self.texto_destino.title()
            
            if inicio not in self.roteador.grafo_obj.dados:  # Se o bairro de partida não existir na nossa base de dados:
                self.atualizar_log("Parada não encontrada no sistema EPT.")  # Mostra erro informando.
                return  # Aborta a execução do clique.
                
            # Chama o algoritmo de Dijkstra no roteador passando os pontos validados.
            tempo, caminho, lines = self.roteador.calcular_caminho(inicio, fim)
            
            if caminho:  # Se um caminho válido foi encontrado pelo roteador:
                dados_grafo = self.roteador.grafo_obj.dados  # Obtém os dados de conexões de ônibus.
                linhas_off = self.roteador.linhas_desativadas  # Obtém a lista de linhas inativas.
                step_descriptions = []  # Inicializa lista de descrições dos passos da rota.
                
                for i in range(len(caminho) - 1):  # Itera sobre cada segmento do trajeto calculado.
                    u, v = caminho[i], caminho[i+1]  # Define o ponto de partida 'u' e o de chegada 'v' do segmento.
                    opcoes = dados_grafo[u][v]  # Pega as opções de transporte de 'u' para 'v'.
                    
                    # Filtra apenas as linhas ativas (removendo as que estão marcadas no conjunto linhas_off)
                    opcoes_ativas = [op for op in opcoes if op["linha"] not in linhas_off]
                    if opcoes_ativas:  # Se houver opções ativas remanescentes nesse trecho:
                        # Descobre qual o menor tempo possível oferecido pelas opções ativas.
                        min_t = min(op["tempo"] for op in opcoes_ativas)
                        # Agrupa todos os nomes de linhas que empatam com esse menor tempo de viagem.
                        linhas_mesmo_tempo = [op["linha"] for op in opcoes_ativas if op["tempo"] == min_t]
                        
                        if len(linhas_mesmo_tempo) >= 2:  # Se houver duas ou mais linhas com o mesmo tempo mínimo:
                            # Agrupa seus nomes no formato "(L1 / L2)".
                            linha_str = f"({ ' / '.join(linhas_mesmo_tempo) })"
                        else:  # Caso haja apenas uma linha campeã em tempo:
                            linha_str = linhas_mesmo_tempo[0]  # Armazena apenas o nome dela.
                        # Adiciona à lista o nome da linha de ônibus seguido do bairro onde ela foi pega '[u]'.
                        step_descriptions.append(f"{linha_str} [{u}]")
                
                caminho_str = " -> ".join(f"Pt {n}" for n in caminho)  # Une os nós do trajeto formatados com setas indicativas.
                linhas_str = " -> ".join(step_descriptions)  # Une as descrições dos ônibus embarcados em sequência.
                # Constrói a mensagem informativa final contendo trajeto, tempo total e a ordem de ônibus com bairros.
                info = f"Rota encontrada!\n\nTrajeto:\n{caminho_str}\n\nTempo: {tempo} min\n\nÔnibus: {linhas_str}"
                self.atualizar_log(info)  # Exibe a string formatada no painel de log com o devido wrap de texto automático.
                self.atualizar_plot(caminho_destacado=caminho)  # Redesenha o grafo com o caminho selecionado em destaque verde.
            else:  # Caso o Dijkstra retorne uma lista vazia (sem conexão ativa possível):
                # Informa ao usuário sobre a ausência de transporte ativo.
                self.atualizar_log("[ALERTA]\nNão há conexão ativa disponível\nentre esses dois pontos!")
                self.atualizar_plot()  # Redesenha o plot limpando qualquer caminho em destaque anterior.
        except ValueError:  # Captura possíveis erros de conversão de valores.
            self.atualizar_log("[ERRO]\nDigite os nomes corretamente!")  # Informa no painel de logs.

    def toggle_linha_click(self, event):  # Método chamado ao clicar no botão "Alternar" (ativar/desativar linha).
        if not self.texto_linha:  # Se o campo de texto da linha estiver vazio:
            self.atualizar_log("[ERRO]\nDigite o número da linha!")  # Informa sobre o campo vazio no log.
            return  # Aborta a execução do método.
            
        linha = self.texto_linha.upper()  # Converte o nome da linha digitada para maiúsculas (Ex: "30e" -> "30E").
        linhas_existentes = self.roteador.grafo_obj.obter_todas_linhas()  # Recupera todas as linhas cadastradas no grafo.
        
        if linha not in linhas_existentes:  # Se a linha digitada não existir no sistema de transporte cadastrado:
            self.atualizar_log(f"[ERRO]\nA Linha {linha} não\nexiste no sistema!")  # Reporta erro.
            return  # Aborta a execução.
            
        reativada = self.roteador.alternar_linha(linha)  # Alterna o estado da linha no roteador e retorna o novo estado.
        
        if reativada:  # Se a linha foi reativada com sucesso:
            # Exibe mensagem amigável informando o restabelecimento da operação da linha.
            self.atualizar_log(f"LINHA REATIVADA:\n\nA Linha {linha} está ativa\ne operando normalmente!")
        else:  # Caso a linha tenha sido suspensa/desativada:
            # Exibe aviso alertando que a linha está suspensa e novos trajetos buscarão alternativas.
            self.atualizar_log(f"FORA DE SERVIÇO:\n\nA Linha {linha} foi desativada.\nO sistema calculará rotas\nalternativas.")
            
        self.atualizar_plot()  # Redesenha o mapa de rotas atualizando o tracejado pontilhado para a linha inativa.


    def configurar_widgets(self):  # Método responsável por criar e posicionar todos os inputs e botões na janela.
        self.ax_txt_origem = plt.axes([0.10, 0.25, 0.10, 0.04])  # Define os eixos geométricos do campo de texto de partida.
        self.box_origem = widgets.TextBox(self.ax_txt_origem, 'Partida: ', initial='')  # Cria o widget TextBox para a partida.
        self.box_origem.on_text_change(self.txt_origem_changed)  # Conecta a alteração do texto ao callback txt_origem_changed.

        self.ax_txt_destino = plt.axes([0.30, 0.25, 0.10, 0.04])  # Define os eixos geométricos do campo de texto de destino.
        self.box_destino = widgets.TextBox(self.ax_txt_destino, 'Destino: ', initial='')  # Cria o widget TextBox para o destino.
        self.box_destino.on_text_change(self.txt_destino_changed)  # Conecta a alteração do texto ao callback txt_destino_changed.

        # DESIGN: Botão de busca Verde vibrante (Sucesso)
        self.ax_btn_buscar = plt.axes([0.42, 0.25, 0.12, 0.04])  # Define a área geométrica do botão "Achar Rota".
        self.btn_buscar = widgets.Button(self.ax_btn_buscar, 'Achar Rota', color="#27AE60", hovercolor="#229954")  # Cria o botão de busca.
        self.btn_buscar.label.set_color("white")  # Define a cor do texto do botão como branca para alto contraste.
        self.btn_buscar.label.set_fontweight("bold")  # Define o estilo da fonte do botão como negrito.
        self.btn_buscar.on_clicked(self.buscar_caminho_click)  # Conecta o clique do botão ao método buscar_caminho_click.

        self.ax_txt_linha = plt.axes([0.10, 0.18, 0.10, 0.04])  # Define os eixos geométricos do campo de entrada da linha de ônibus.
        self.box_linha = widgets.TextBox(self.ax_txt_linha, 'Linha: ', initial='')  # Cria o widget TextBox correspondente.
        self.box_linha.on_text_change(self.txt_linha_changed)  # Associa a mudança de texto ao callback txt_linha_changed.

        # DESIGN: Botão de alternar Laranja (Aviso/Modificação de rede)
        self.ax_btn_toggle = plt.axes([0.22, 0.18, 0.12, 0.04])  # Define a área geométrica do botão "Alternar".
        self.btn_toggle = widgets.Button(self.ax_btn_toggle, 'Alternar', color="#F39C12", hovercolor="#D68910")  # Cria o botão de alternar estado.
        self.btn_toggle.label.set_color("white")  # Define texto na cor branca.
        self.btn_toggle.label.set_fontweight("bold")  # Aplica negrito à fonte do botão.
        self.btn_toggle.on_clicked(self.toggle_linha_click)  # Conecta o clique ao callback toggle_linha_click.




    def iniciar(self):  # Método simples de ativação da interface gráfica.
        plt.show()  # Exibe a janela gráfica Matplotlib construída na tela e inicia o loop de eventos padrão.