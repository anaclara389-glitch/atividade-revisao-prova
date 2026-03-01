#Monitoramento de Temperatura de Forno Industrial
import time
temperaturas = []

def media_t(temperaturas):
    media = sum (temperaturas) / len(temperaturas)
    return f"A média das temperaturas foi: {media:.2f}"

def alerta(temperaturas):
    cont = 0 #Vai contar quantas vezer a temperatura excedeu o limite
    for temperatura in temperaturas:
        if temperatura > 500: #O limite da temperatura é 500
            cont += 1
    return f"A temperatura exedeu o limite (500°C) {cont} vezes!"

def maior_e_menor(temperaturas):
    return f"A temperatura mais alta registrada foi de: {max(temperaturas)}\n A temperatura mais baixa registrada foi de: {min(temperaturas)}"

while True:
    try: # Se a pessoa digitar algo errado, o programa vai exibir uma mensagem pedindo para o usuário tentar novamente caso haja algum erro
        while len(temperaturas) < 6: #vai adicionando temperaturas, mas para quando chegar em 6 leituras
            temperatura = float(input("Digite a temperatuda do forno industrial em °C: "))
            temperaturas.append(temperatura)
        
        print("-----Relatório-----") #mostrando o relatório no terminal
        print(f"As temperaturas registradas foram: {temperaturas}")
        print("-----")
        print(media_t())
        print(alerta())
        print(maior_e_menor(temperaturas))
        print("-----")
        
        time.sleep(2) #O programa vai esperar 2 segundo antes de mostrar a pergunta no terminal
        resposta = input("Deseja fazer um novo registro (s/n): ")
        if resposta == "s":
            temperaturas = []
        elif resposta == "n":
            print("Não deseja fazer novo registro, saindo do programa...")
            time.sleep(2) #O programa vai esperar 2 segundo antes de mostrar a pergunta no terminal
            break
        else:
            print("Resposta inválida")
    except:
        print("Tente novamente")