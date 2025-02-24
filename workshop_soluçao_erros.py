"""#ex1
print("Olá, mundo!")"""

"""#ex2
nome = "Davi"
print(nome)"""

"""#ex3
def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)"""

"""#ex4
while True:
    try:
        numeros = [10, 20, 30]
        indice = int(input("Digite um índice para acessar a lista: ")) 
        print(numeros[indice])
    except ValueError:
        print("Índice fora dos limites")
    except IndexError:
        print("Índice fora dos limites")"""

"""#ex5
def dividir(a, b):
    return a / b
while True:
    try:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        resultado = dividir(int(num1), int(num2))
        print(f"Resultado: {resultado:.2f}")
    except ValueError:
        print("Valor Inválido")
    except ZeroDivisionError:
        print("Não é possível dividir por 0")"""

"""#ex6
while True:
    try:
        dados = {
        "nome": "Isaac ",
        "idade": 25,
        "cidade": "São Paulo"
        }
        chave = input("Digite a chave que deseja acessar: ")
        print(f"O valor da chave '{chave}' é: {dados[chave]}")
        break
    except KeyError:
        print("Valor da chave Inválido")"""
"""#ex7
while True:
    try:
        def validar_idade(idade):
            if idade < 0 or idade > 120:
                raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
            return f"Idade válida: {idade}"

        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
    except ValueError:
        print("A idade deve estar entre 0 e 120 anos!")"""

"""#ex8
def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = [8, 9, '10', 7]
notas = list(map(int, notas))
media = calcular_media(notas)
print(f"Média: {media:.2f}")"""