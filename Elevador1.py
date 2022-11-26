print("Simulador de Elevador\n")

print("O elevador tem suporte de ate 20 pessoas com pesso maximo de 1000kg")
print("O prédio possui 15 andares e dois subsolos (garagem)\n")

pessoa_andar = {}
pessoa_peso ={}

pessoas = int (input("Quantas pessoas entraram no elevador? \n"))
andar = 0
andares = []
peso = 0
peso_total = 0

for pessoa in range(1 , pessoas+1):
    if pessoas > 20:
        print("exesso de passageiros")

    else:
        andar = int(input(f"{pessoa}° pessoa, qual o andar desejado? "))
        if andar < -2 or andar > 15:
            print("Andar invalido")
            continue

        else:
            pessoa_andar[pessoa] = andar
            andares.append(andar)
            andares.sort()
            print(pessoa_andar)
            

            peso = float (input(f"Digite o Peso da {pessoa}° pessoa: "))
            peso_total = peso_total + peso
            if peso_total > 1000:
                print("Peso exedido")
                continue
            else:
                pessoa_peso[pessoa] = peso
                print(pessoa_peso)
                index =0 
                for andar in andares:
                    if peso_total <=1000 or pessoa <= 20:
                        print(f" Elevador esta subindo para o {andares[index]}° andar ")
                        index += 1
                    if pessoa_andar.get(andar):
                        print(f"passageiros {pessoa_andar} chegaram ao andar {andares}")
                    else:
                        continue

                        