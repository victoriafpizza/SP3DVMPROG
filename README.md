# SP3DVMPROG

ERIC RODRIGUES rm550249
FERNANDO POPOLILI rm99919
HENRIQUE DE BRITO rm98831
RODRIGO LIMA rm98326
VICTORIA FRANCESCHINI rm550609

## **Introdução**

O desenvolvimento de jogos de Realidade Virtual (VR) tem crescido exponencialmente, permitindo que diversas áreas utilizem essa tecnologia para treinamentos práticos. Este projeto apresenta um jogo de VR focado no treinamento de coordenação manual dos jogadores. O jogo é baseado em uma simulação onde os usuários interagem com uma tela de pintura virtual, realizando traços precisos para alcançar pontuações altas. A principal finalidade do jogo é avaliar e melhorar a coordenação motora dos jogadores, fornecendo feedback visual e estatístico em tempo real.

## **Metodologia**

### **Estrutura do Jogo**
O jogo simula um ambiente de pintura virtual onde os jogadores devem traçar formas específicas na tela com precisão e no menor tempo possível. O jogador é pontuado com base em três critérios:
1. **Pontuação do traço**: Cada traço correto recebe uma pontuação.
2. **Tempo de execução**: Traços realizados rapidamente aumentam a pontuação.
3. **Precisão do traço**: Quanto mais o traço se assemelhar ao modelo proposto, maior será a pontuação.

### **Estruturas de Dados**
Para armazenar os resultados de cada tentativa, utilizamos duas classes:
- **Classe `Jogador`**: Cada jogador tem um nome e uma lista de tentativas, onde cada tentativa armazena dados de pontuação, tempo de execução e precisão.
- **Classe `Jogo`**: Armazena todos os jogadores e controla a adição de novas tentativas e a exibição dos resultados.

### **Armazenamento e Cálculo de Pontuação**
Os dados de cada tentativa são armazenados em dicionários, permitindo que o jogo armazene informações detalhadas sobre cada jogada (pontuação, tempo, precisão). A pontuação média de cada jogador é calculada a partir da soma das pontuações de todas as tentativas, dividida pelo número de tentativas.

#### Exemplo de Estrutura de Dados:
```python
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tentativas = []

    def adicionar_tentativa(self, pontuacao, tempo, precisao):
        tentativa = {
            "pontuacao": pontuacao,
            "tempo": tempo,
            "precisao": precisao
        }
        self.tentativas.append(tentativa)

    def calcular_media_pontuacao(self):
        return sum(t['pontuacao'] for t in self.tentativas) / len(self.tentativas)

class Jogo:
    def __init__(self):
        self.jogadores = {}

    def adicionar_jogador(self, nome):
        self.jogadores[nome] = Jogador(nome)
```

## **Resultados**

Durante o desenvolvimento e testes do jogo, dois jogadores foram inseridos no sistema, "João" e "Maria". Foram registradas três tentativas para cada jogador, com suas respectivas pontuações, tempos de execução e precisões.

### **Exemplo de Pontuações Registradas:**
- **João**:
  - Tentativa 1: 85 pontos, 30 segundos, 90% de precisão
  - Tentativa 2: 90 pontos, 28 segundos, 95% de precisão
  - Tentativa 3: 78 pontos, 35 segundos, 85% de precisão
  - **Pontuação Média**: 84.33

- **Maria**:
  - Tentativa 1: 70 pontos, 32 segundos, 88% de precisão
  - Tentativa 2: 88 pontos, 25 segundos, 92% de precisão
  - Tentativa 3: 82 pontos, 29 segundos, 89% de precisão
  - **Pontuação Média**: 80

Os resultados mostram que a pontuação média dos jogadores varia de acordo com o tempo e a precisão dos traços. "João" teve uma performance ligeiramente melhor, com uma média de 84.33, enquanto "Maria" alcançou 80.

## **Conclusão**

Este projeto demonstrou a eficiência de um jogo de VR para treinamento de coordenação manual, armazenando e analisando dados detalhados de cada tentativa de traço dos jogadores. O jogo pode ser uma ferramenta valiosa para treinar habilidades motoras finas em ambientes virtuais, fornecendo feedback contínuo para os usuários. 

### **Melhorias Futuras**
Algumas melhorias podem ser implementadas, como:
- Adicionar mais métricas para avaliação, como resistência do jogador e evolução ao longo do tempo.
- Incluir modos de dificuldade ajustáveis para adaptar a experiência às necessidades dos jogadores.
- Expandir o uso da plataforma para diferentes tipos de treinamentos em ambientes de VR.
