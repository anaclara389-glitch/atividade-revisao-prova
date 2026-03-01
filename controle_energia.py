# Controle de Consumo de Energia (Célula de Produção)
import time
consumos = []

def total(consumos):
    return f"A soma total de consumo é {sum(consumos)}"

def maior_gasto(consumos):
    return f"O maior consumo é: {max(consumos)}"

def calcular_custo(consumos):
    custo = sum(consumos) * 0.85
    return f"O valor total de custos é R${custo:.2f}"

while True:
    try:
        for i in range(4):
            registro = float(input(f"Digite o consumo de energia (kWh) da {i + 1}ª máquina: "))
            consumos.append(registro)
            
        print("-"*15,"Relatório","-"*15)
        time.sleep(0.3)
        print(total(consumos))
        print(maior_gasto(consumos))
        print(calcular_custo(consumos))
        print("-"*30)
        
        opcao = input("Deseja fazer outro registro? (s/n): ")
        if opcao == 'n':
            print("Finalizando sistema... Até logo!")
            time.sleep(0.8)
            break
        elif opcao == 's':
            consumos = []
        else:
            print("Resposta inválida")
            break
    except ValueError:
        print("Tente novamente")
    