# Solicita ao usuário que insira seu peso em quilogramas e altura em metros
peso = float(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite a sua altura em metros: '))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado com duas casas decimais
print('Seu IMC é: {:.2f}'.format(imc))

# Interpretação do IMC
if imc < 18.5:
    print("Você está abaixo do peso normal.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está saudável.")
elif 24.9 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")