print("O programa calcula a quantidade de rodapé e a quantidade de piso de uma sala retangular: ")

comp= float(input("Digite o comprimento da sala em métros: "))
larg= float(input("Digite a largura da sala em métros: "))

qtdPiso= comp * larg
qtdRodape= (comp *2) + (larg * 2)

print("A quantidade de piso é: ", qtdPiso)
print("A quantidade de rodapé é: ", qtdRodape, "m")