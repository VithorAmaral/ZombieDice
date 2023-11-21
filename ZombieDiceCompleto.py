"""
Aluno: Vithor Pinto da Cruz do Amaral
Curso: Analise e Desenvolvimento de Sistemas
Matéria: Raciocínio Computacional
Turma: (11100010563_20221_01)
Professor: Galbas Milleo Filho
"""

# Importa a biblioteca random com shuffle(embaralhar) e choice(escolher)
from random import shuffle, choice

# Importa a biblioteca collection com o namedtuple para criar tuplas com campos nomeados
from collections import namedtuple

# Importa a biblioteca tempo
import time


# Função para criar os dados
def criar_dados():
    # Tupla dados com os atributos de cor e lado
    Dado = namedtuple("Dado", ['cor', 'lados'])
    # Tupla do dado verde com todas as faces possíveis
    dado_verde = Dado('verde', ['cerebro', 'cerebro', 'cerebro', 'passo', 'passo', 'tiro'])
    # Tupla do dado vermelho com todas as faces possíveis
    dado_vermelho = Dado('vermelho', ['cerebro', 'passo', 'passo', 'tiro', 'tiro', 'tiro'])
    # Tupla do dado amarelo com todas as faces possíveis
    dado_amarelo = Dado('amarelo', ['cerebro', 'cerebro', 'passo', 'passo', 'tiro', 'tiro'])

    # Colocando os dados na lista
    lista_dados = []
    # Adiciona 6 dados verdes na lista
    for _ in range(6):
        lista_dados.append(dado_verde)
    # Adiciona 3 dados vermelhos na lista
    for _ in range(3):
        lista_dados.append(dado_vermelho)
    # Adiciona 4 dados amarelos na lista
    for _ in range(4):
        lista_dados.append(dado_amarelo)

    # Embaralha a lista com os 13 dados dentro e retorna a lista
    shuffle(lista_dados)
    return lista_dados


# Função para criar o jogador
def criar_jogadores():
    # Lista de jogadores começa vazia
    jogadores = []

    while True:
        try:
            # Pergunta ao usuario o número de jogadores
            num_jogadores = int(input("Digite o numero de jogadores: "))
            # Se for maior que 1 ele começa o programa
            if num_jogadores > 1:
                break
            # Senão manda mensagem de erro e repete a pergunta de quantos jogadores são
            else:
                print("Valor mínimo de jogadores é 2!")
        # Se o usuario não usar um número inteiro ele manda mensagem de erro.
        except ValueError:
            print("O número precisa ser um inteiro.")

    # Pergunta ao usuario o nome do jogador conforme o tanto de jogadores que tem
    for i in range(num_jogadores):
        nome = input(f'Digite o nome do {i + 1}° jogador: ').capitalize()  # Transforma a primeira letra em maiuscula
        # A variavel jogador recebe o nome e a pontuação inicial que é 0
        jogador = {'nome': nome, 'pontuacao': 0}
        # Adiciona a variavel jogador na lista jogadores
        jogadores.append(jogador)

    # Embaralha a lista jogadores para ver quem vai começar
    shuffle(jogadores)
    print("~/~/~ ORDEM DE JOGADORES ~/~/~")
    # Mostra a posição e o nome do jogador em ordem de quem vai jogar
    pos = 1
    for jogador in jogadores:
        print(f"{pos}. {jogador['nome']}")
        pos += 1

    # Retorna a lista jogadores
    return jogadores


# Função para cada turno de jogador
def rodada(jogador):
    # Mostra na tela de quem é a vez de jogar e espera 1 segundo
    print(f"\nVez do jogador {jogador['nome']}")
    time.sleep(1)

    # lista_dados recebe a lista de dados embaralhados
    lista_dados = criar_dados()
    # Pontuação temporaria para cada turno, começa com 0
    pontuacao_temp = {'cerebros': 0, 'tiros': 0}
    # Para começar a jogar precisa de tres dados na mão, sendo esta lista, comecando vazia
    dados_na_mao = []

    while True:
        # Enquanto tiver menos de 3 dados na mão, tira da lista de dados e coloca na mão do usuario
        while len(dados_na_mao) < 3:
            dados_na_mao.append(lista_dados.pop())

        # Mostra para o usuario qual dado está sendo jogado
        n = 1
        for dado in reversed(dados_na_mao):
            time.sleep(0.5)
            print(f"Jogando dado {n}")
            n += 1

            # Pega a cor do dado que está sendo utilizado
            cor = dado.cor
            # Embaralha as faces do dado atual
            shuffle(dado.lados)
            # O lado sorteado recebe a escolha do embaralhamneto do lado dos dados
            lado_sorteado = choice(dado.lados)

            # Mostra para o usuario a cor do dado e o lado do respectivo dado
            print(f"   Cor: {cor}\n   Lado: {lado_sorteado}")

            # Verificar dados
            # Se o lado cair cerebro, adiciona +1 cerebro a pontuação temporaria
            if lado_sorteado == 'cerebro':
                pontuacao_temp['cerebros'] += 1
                # Como não é passo, tiro o dado da mão e devolvo para o copo
                lista_dados.append(dados_na_mao.pop(dados_na_mao.index(dado)))
            # Se o lado cair tiro, adiciona +1 tiro a pontuação temporaria
            elif lado_sorteado == 'tiro':
                pontuacao_temp['tiros'] += 1
                # Como não é passo, tiro o dado da mão e devolvo para o copo
                lista_dados.append(dados_na_mao.pop(dados_na_mao.index(dado)))
            # Embaralha a lista de dados de novo
            shuffle(lista_dados)

        #  Mostra para o usuario os cerebros atuais e os tiros atuais
        print(f"\nCérebros atuais: {pontuacao_temp['cerebros']}\nTiros atuais: {pontuacao_temp['tiros']}")
        # Se a pontuação temporaria for menor que 3, pergunta se o usuario que continuar
        if pontuacao_temp['tiros'] < 3:
            # Se a resposta diferir de sim, a tela mostra a pontuação de cerebros que o usuario conseguiu
            if input("\nVoce gostaria de jogar novamente?(S/N): ").upper().strip() != 'S':
                print(f"Você conseguiu {pontuacao_temp['cerebros']} cérebros.")
                # Os cerebros que o jogador conseguiu na rodada são adicionados na pontuação final
                jogador['pontuacao'] += pontuacao_temp['cerebros']
                # Muda para o turno do outro jogador
                break
        # Se o jogador tomar mais de 3 tiros, ele perde todos os cerebros que conseguiu na rodada
        else:
            print(f"Você tomou muitos tiros e foi a bigodar. {pontuacao_temp['cerebros']} cérebros.")
            # E muda para o turno do outro jogador
            break


# Função para mostrar o placar atual de cada jogador
def placar(jogadores):
    print("\n~/~/~ COM QUANTOS PONTOS CADA JOGADOR ESTÁ? ~/~/~")
    # Conforme o número de jogadores, mostra o nome e a pontuação de cada jogador
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontuacao']} pontos.")


# Programa Principal
jogadores = criar_jogadores()

# Fim de jogo começa como falso
fim_de_jogo = False
# Enquanto não terminou o jogo, cada jogador tem uma rodada
while not fim_de_jogo:
    for jogador in jogadores:
        rodada(jogador)
        # Se o jogador tiver uma pontuação de 13 ou mais, esse mesmo jogador é o vencedor
        if jogador['pontuacao'] >= 13:
            vencedor = jogador['nome']
            # E assim acaba o jogo
            fim_de_jogo = True
    # Se não acabou o jogo, o programa continua a mostrar o placar a cada fim de rodada
    if not fim_de_jogo:
        placar(jogadores)
    # Se acabou o jogo, o programa mostra a mensagem de quem venceu e mostra o placar final
    else:
        print(f"\n{vencedor} do Brasil!!!! Parabéns, você venceu!!!")
        placar(jogadores)
