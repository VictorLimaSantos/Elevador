print("Simulador de Elevador\n")

print("O elevador tem suporte de ate 20 pessoas com pesso maximo de 1000kg")
print("O prédio possui 15 andares e dois subsolos (garagem)\n")

andares = []
peso = 0
peso_total = 0
for count in range(-2, 16):
    if count < 0:
        print(f"subsolo G{count}")
    elif count == 0:
        print("Terreo")
    elif count <=15:
        print(f"{count}° Andar")

pessoas = int (input("Quantas pessoas entraram no elevador? \n"))

for pessoa in range(1 , pessoas+1):

    if pessoas > 20:
        print("exesso de passageiros")
        break
    andar = int(input(f"{pessoa}° pessoa, qual o andar desejado? "))
    andares.append(andar)
    andares.sort()

    peso = float (input(f"Digite o Peso da {pessoa}° pessoa: "))
    peso_total = peso_total + peso
    if peso_total > 1000:
        print("Peso exedido")
        break
    
    index = 0
    for andar in andares:
        if peso_total <=1000 and pessoa <= 20:
            print(f" Elevador esta subindo para o andar {andares[index]}")
            index += 1
    





