capital = float(input("Digite o capital inicial: "))
taxaJuros = float(input("Digite a taxa de juros anual (em decimal): "))
tempo = float(input("Digite o tempo em anos: "))

juros = capital * taxaJuros * tempo

montanteTotal = capital + juros

print(f"O montante total após {tempo} anos é: {montanteTotal}")