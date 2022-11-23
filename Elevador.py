print("Simulador de Elevador:")

print("O elevador tem suporte de ate 20 pessoas com pesso maximo de 1000kg")
print("O prédio possui 15 andares e dois subsolos (garagem)")
andares = []
peso = []
for count in range(-2, 16):
    if count < 0:
        print(f"subsolo G{count}")
    elif count == 0:
        print("Terreo")
    elif count <=15:
        print(f"{count}° Andar")

pessoas = int (input("Quantas pessoas entraram no elevador? "))


for pessoa in range(0 , pessoas):
    andar = int(input(f"{pessoa+1}° pessoa, qual o andar desejado? "))
    andares.append(andar)
    andares.sort()
    peso





