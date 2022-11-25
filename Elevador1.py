print("Simulador de Elevador\n")

print("O elevador tem suporte de ate 20 pessoas com pesso maximo de 1000kg")
print("O prédio possui 15 andares e dois subsolos (garagem)\n")

pessoa_andar = {}
pessoa_peso ={}

pessoas = int (input("Quantas pessoas entraram no elevador? \n"))
andares = 0
peso = 0
peso_total = 0

for pessoa in range(1 , pessoas+1):
    if pessoas > 20:
        print("exesso de passageiros")

    else:
        andares = int(input(f"{pessoa}° pessoa, qual o andar desejado? "))
        if andares < -2 or andares > 15:
            print("Andar invalido")
            continue

        else:
            pessoa_andar[pessoa] = andares
            print(pessoa_andar)

            peso = float (input(f"Digite o Peso da {pessoa}° pessoa: "))
            peso_total = peso_total + peso
            if peso_total > 1000:
                print("Peso exedido")
                continue
            else:
                pessoa_peso[pessoa] = peso
                print(pessoa_peso)
            index = 0
            for andar in andares:
                if peso_total <=1000 and pessoa <= 20:
                    print(f" Elevador esta subindo para o andar {andares[index]}")
                    index += 1
                
