valorConta = float(input("Digite o valor total da conta: "))
porcGorjeta = float(input("Digite a porcentagem de gorjeta: "))

gorjeta = valorConta * (porcGorjeta / 100)

totalPago = valorConta + gorjeta

print(f"Valor da gorjeta: {gorjeta}")
print(f"Total a ser pago: {totalPago}")