# main.py - Arquivo principal responsável pela inicialização e execução do programa.

import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para renderização de gráficos e interface visual.

# Importa a classe Grafo que contém a representação das rotas, bairros, tempos e linhas.
from regras_e_logica.grafo import Grafo  
# Importa a classe Roteador que contém a lógica de cálculo de caminho mínimo (Dijkstra).
from regras_e_logica.roteador import Roteador  
# Importa a classe InterfaceEPT que cria e gerencia os componentes da interface visual da EPT.
from ui_interface_usuario.interface import InterfaceEPT  


def main():
    # Cria uma instância da classe Grafo para carregar os bairros, conexões e linhas de ônibus ativos.
    meu_grafo = Grafo()  
    
    # Cria uma instância do Roteador, injetando o objeto de grafo criado anteriormente para cálculo de rotas.
    meu_roteador = Roteador(meu_grafo)  
    
    # Cria a interface do usuário (GUI), injetando o roteador que a interface chamará para calcular os caminhos.
    app = InterfaceEPT(meu_roteador)  
    
    # Inicia o loop de exibição e interação da janela matplotlib, abrindo a aplicação para o usuário.
    app.iniciar()  

# Ponto de entrada padrão do Python: executa a função main() apenas se o arquivo for executado diretamente.
if __name__ == "__main__":
    main()  