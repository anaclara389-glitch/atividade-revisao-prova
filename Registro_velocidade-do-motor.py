#Registro de velocidade do motor
valores = [] #lista vazia
        
def media(valores): #calculando a média
    media = sum(valores) / len(valores)
    return f"A média da velocidade do motor é: {media:.2f}"#:.2f vai mostrar a média com apenas 2 casas atrás da vírgula

def maior_valor(valores): #calculando o maior valor
    maior = max(valores)
    return f"A maior velocidade do motor registrada foi: {maior}"

def menor_valor(valores): #calculando menor valor
    menor = min(valores)
    return f"A menor velocidade do motor registrada foi:{menor}"

def total(valores): #calculando o total
    soma = sum(valores)
    return f"A soma total dos valores foi: {soma}"

while True: #loop while para poder repetir a ação caso o usuário queira continuar
    try:
        while len(valores) < 5: #loop para adicionar cada vez mais itens a lista (desde que menor do que 5)
            valor = float(input("Digite a velocidade do Motor: "))
            valores.append(valor) #adicionar valores a lista
         
        print("-----Relatório Final-----")
        print(f"Os valores registrados foram: {valores}")
        print("-----")
        print(media(valores))
        print(maior_valor(valores))
        print("-----")
        print(menor_valor(valores))
        print(total(valores))

        resposta = input("Deseja realizar nova coleta? (s/n)") #aqui o usuário vai dizer se deseja continuar
        if resposta == "s":
            valores = [] #zerando a lista
            print("Você aceitou fazer nova coleta de dados.")
            print('-----')
        elif resposta == "n":
                print("Você escolheu sair.") #Saindo do código 
                break
    except:
        print("\033[31mTente novamente\033[m") #Texto com uma cor viva(vermelho) para mostrar o erro mais facilmente