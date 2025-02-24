from random import randint

def linhas():
    print("-="*24)

def escolha_ppt(pergunta="Qual a sua escolha? "):
    while True:
        try:
            resposta = input(pergunta)
            conversao = int(resposta)
            if conversao == 0 or conversao == 1 or conversao == 2:
                return conversao
            else:
                print("\nDigite um número válido\n[0]Pedra\n[1]Papel\n[2]Tesoura\n")
        except ValueError:
            print("\nDigite um Número Válido\n[0]Pedra\n[1]Papel\n[2]Tesoura\n")

def ppt():
    linhas()
    itens = ('Pedra', 'Papel', 'Tesoura')
    print('[0]Pedra\n[1]Papel\n[2]Tesoura')
    jogador1 = escolha_ppt()
    computador1 = randint(0, 2)
    linhas()
    print('Jogador jogou {}\nComputador Jogou {}'.format(itens[jogador1], itens[computador1]))
    linhas()
    if (jogador1 == 0 and computador1 == 2) or (jogador1 == 1 and computador1 == 0) or (jogador1 == 2 and computador1 == 1):
        print('Jogador Vence!')
    elif jogador1 == computador1:
        print('!EMPATE!')
    else:
        print('Computador Vence!')

def escolha_ip(pergunta="Qual sua escolha? "):
    while True:
        try:
            valor = input(pergunta)
            conversao = int(valor)
            if conversao == 0 or conversao == 1:
                return conversao
            else: 
                print("Resposta Inválida")
        except ValueError:
            print("Resposta Inválida")

def valor_escolha(pergunta="Escolha um número: "):
    while True:
        try:
            valor = input(pergunta)
            conversao = int(valor)
            return conversao
        except ValueError:
            print("Resposta Inválida")

def ip():
    linhas()
    itens = ('Par', 'Ímpar')
    print('[0]Par\n[1]Ímpar')
    linhas()
    jogador2 = escolha_ip()
    numero1 = valor_escolha()
    computador2 = randint(0, 10)
    soma = 0 if (computador2 + numero1) %2 == 0 else 1
    linhas()
    print('Jogador jogou {}\nComputador jogou {}'.format(numero1, computador2))
    linhas()
    resultado = itens[soma]
    print(f'O resultado é {resultado}')
    if soma == jogador2:
        print('Jogador Vence!')
    else:
        print('Computador Vence!')
    linhas()
    
def oquejogar(pergunta="O que Você quer jogar:\n[0] Pedra-Papel-Tesoura\n[1] Ímpar our Par\n--> "):
    while True:
        try:
            linhas()
            querjogar = input(pergunta)
            conversao = int(querjogar)
            if conversao == 0:
                ppt()
            elif conversao == 1:
                ip()
            else: 
                print("Resposta Inválida")
            break
        except ValueError:
            print("Resposta Inválida")
        
def playagain(teste="Você quer jogar de novo? [s/n] "):  
    while True:
        try:
            jogardnv = input(teste)
            if jogardnv == 's':
                return 's'
            elif jogardnv == 'n':
                print('Obrigado por Jogar')
                return 'n'
            else:
                print("Resposta Inválida")
        except ValueError:
            print("Resposta Inválida")
        break
def main():
    while True:
        print(oquejogar())
        print(playagain())
        a = playagain()
        if a == 'n':
            break
main()        
