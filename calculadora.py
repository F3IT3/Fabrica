def linhas():
    print("-="*16)
    
class Calculadora():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def somar(self):
        soma = self.n1 + self.n2
        somahistorico = (f"{self.n1} + {self.n2} = {soma}")
        return somahistorico
    def subtrair(self):
        subtrai = self.n1 - self.n2
        subtrai_historico = (f"{self.n1} - {self.n2} = {subtrai}")
        return subtrai_historico
    def multiplicar(self):
        multiplica = self.n1 * self.n2
        multiplica_historico = (f"{self.n1} * {self.n2} = {multiplica}")
        return multiplica_historico
    def dividir(self):
        divida = self.n1 / self.n2
        divida_historico = (f"{self.n1} / {self.n2} = {divida:.2f}")
        return divida_historico
    
def main():
    historico = []   
    while True:
        try:
            linhas()
            print("CALCULADORA")
            linhas()
            operacao = int(input("[0] Somar\n[1] Subtrair\n[2] Multiplicar\n[3] Dividir\n[4] Ver Histórico\n[5] Apagar Histórico\n[6] Fechar Calculadora\n -> "))    
            linhas()
            if operacao == 0 or  operacao == 1 or operacao == 2 or operacao == 3:
                numero1 = int(input("Escolha um número: "))
                numero2 = int(input("Escolha um número: "))
                c1 = Calculadora(numero1, numero2)
                try:
                    if operacao == 0:
                        print(c1.somar())
                        h1 = c1.somar()              
                    elif operacao == 1:
                        print(c1.subtrair())
                        h1 = c1.subtrair()
                    elif operacao == 2:
                        print(c1.multiplicar())
                        h1 = c1.multiplicar()
                    elif operacao == 3:
                        print(c1.dividir())
                        h1 = c1.dividir()
                    historico.append(h1)
                except ZeroDivisionError:
                    print("\033[31m Resposta Inválida \033[37m")
            elif operacao == 4:
                if historico == []:
                    print("Histórico Vazio")
                else:
                    print(historico)
            elif operacao == 5:
                historico.clear()
                print("Histórico Apagado")
            elif operacao == 6:
                print("Fim da Operação")
                break
            else:
                print("\033[31m Resposta Inválida: \033[37m")
        except ValueError:
            print("\033[31m Resposta Inválida \033[37m")

if __name__ == "__main__":
    main()