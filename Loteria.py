import random
num = random.randint(1,100)
tentativa = int(input("Teste a sua sorte, digite um numero inteiro de 1 a 100: "))

match num:
    case num if num == tentativa:
        print("Parabens você é um cagão!")
    case default:
        print(f"Errooou!!, o numero sorteado era: {num}")