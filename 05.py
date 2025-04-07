'''5. Construir um programa que leia um conjunto de caracteres (uma frase, terminada por
“Enter”) da entrada padrão e ao final imprima o número de caracteres lidos.'''

while True:

    print("-" * 50)
    print(" " * 19, "𝗖𝗢𝗡𝗧𝗔𝗗𝗢𝗥")
    print("-" * 50)

    frase = str(input("Insira uma frase e quando terminar. Digite “Enter”: \n"))
    acumulador = 0

    for char in frase:
        acumulador += 1

    print(f"Sua frase possui {acumulador} caracteres.")
    print("-" * 50)
    
    continuar = str(input("Deseja continuar a escrever? (Sim/Não): \n")).lower()
    
    if continuar == "nao" or continuar == "não":
        print("Obrigado por utilizar o programa.")
        print("-" * 50)
        break
    elif continuar == "sim":
        print("-" * 50)
        continue
    else:
        print("Devido à entrada incorreta, iremos reiniciar o programa.")
        print("-" * 50)
        continue
