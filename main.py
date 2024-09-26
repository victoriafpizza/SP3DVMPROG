class Jogador:
    """Representa um jogador do jogo."""

    def __init__(self, nome):
        """Inicializa um novo jogador com um nome."""
        self.nome = nome
        self.pontuacoes = []

    def adicionar_pontuacao(self, pontuacao):
        """Adiciona uma nova pontuação ao jogador."""
        self.pontuacoes.append(pontuacao)

    def calcular_media_pontuacao(self):
        """Calcula a média das pontuações do jogador."""
        if len(self.pontuacoes) == 0:
            return 0
        return sum(self.pontuacoes) / len(self.pontuacoes)

class Jogo:
    """Representa o jogo de pintura virtual."""

    def __init__(self):
        """Inicializa um novo jogo."""
        self.jogadores = {}  # Dicionário para armazenar os jogadores

    def adicionar_jogador(self, nome):
        """Adiciona um novo jogador ao jogo."""
        if nome not in self.jogadores:
            self.jogadores[nome] = Jogador(nome)
        else:
            print(f"O jogador {nome} já existe!")

    def registrar_pontuacao(self, nome_jogador, pontuacao):
        """Registra a pontuação de um jogador."""
        if nome_jogador in self.jogadores:
            self.jogadores[nome_jogador].adicionar_pontuacao(pontuacao)
        else:
            print(f"O jogador {nome_jogador} não está no jogo!")

    def exibir_resultados(self):
        """Exibe os resultados de todos os jogadores."""
        for nome_jogador, jogador in self.jogadores.items():
            media = jogador.calcular_media_pontuacao()
            print(f"Jogador: {nome_jogador}, Pontuação Média: {media}")

# Criando um novo jogo
jogo = Jogo()

# Adicionando jogadores
jogo.adicionar_jogador("João")
jogo.adicionar_jogador("Maria")

# Registrando pontuações
jogo.registrar_pontuacao("João", 85)
jogo.registrar_pontuacao("João", 90)
jogo.registrar_pontuacao("João", 78)
jogo.registrar_pontuacao("Maria", 70)
jogo.registrar_pontuacao("Maria", 88)
jogo.registrar_pontuacao("Maria", 82)

# Exibindo os resultados
jogo.exibir_resultados()
