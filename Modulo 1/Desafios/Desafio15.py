km=float(input("Quantos km foram percorridos com o carro? "))
dias=int(input("O carro ficou alugado por quantos dias? "))

print(f"Diaria: R${dias*60:.2f} \nPreço por km: R${km*0.15:.2f} \nTotal: R${(dias*60)+(km*0.15):.2f}")