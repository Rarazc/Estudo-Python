nome= input("nome: ")
idade= int(input("idade: "))
peso= int(input("peso: "))
altura= float(input("altura: "))
imc = peso/(altura ** 2)

print("Dados do imc do paciente: {:=^20}".format(nome))

match imc:
    case imc if 17 <= imc <= 18.4:
        print('abaixo do peso')
    case imc if 18.5 <= imc <= 24.9:
        print('Peso normal')
    case imc if 25 <= imc <= 29.9:
        print('Acima do peso')
    case imc if 30 <= imc <= 34.9:
        print('obesidade grau 1')
    case imc if 35 <= imc <= 40:
        print('Obesidade grau 2')
    case imc if imc >=40:
        print('Obesidade grau 3')