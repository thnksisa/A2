'''2. Um dado material radioativo perde metade de sua massa a cada 50 s. Dada a massa
inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
essa massa seja menor que 0,5g. '''

# CONSTANTES:

massa_final = 0.5
tempo_final = 0

# INÍCIO:

print("PROGRAMA QUE DEFINE A DECADÊNCIA DE UM MATERIAL RADIOATIVO: \n ")


while True:
    massa_inicial = input("Insira a quantidade aproximadamente da massa em gramas: ")

    numero = massa_inicial.isnumeric()

    if numero == True:
        massa_inicial = float(massa_inicial)
        if massa_inicial > 0 and massa_inicial < 0.5:
            print("Não é necessário tempo para decadência radioativa. A massa é menor do que 0,5 gramas.")
        else:
            while massa_inicial > massa_final:
                    massa_inicial /= 2
                    tempo_final += 50
            print(f"O tempo necessário para que haja decadência radioativa é de: {tempo_final} segundos.")
            break
    
    else:
        print("Insira um DÍGITO POSITIVO e INTEIRO, por favor!!!!!!!!")