valorProd = float(input("Digite o valor do produto: "))
porcDesconto = float(input("Digite a porcentagem de desconto: "))

desconto = valor_produto * (porcDesconto / 100)
precComDesc = valorProd - desconto

print(f"O preço com desconto é: {precComDesc:.2f}")