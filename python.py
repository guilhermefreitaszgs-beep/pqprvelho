# Imprimir na tela
print("Olá, Python!")

# Variáveis
nome = "João"
idade = 25
altura = 1.75
ativo = True

# Tipos de dados
tipo_texto = type("texto")
tipo_numero = type(42)

# Operações matemáticas
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
resto = 10 % 3
potencia = 2 ** 3

# Entrada de dados
entrada = input("Digite algo: ")

# Condicionais
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Loops
for i in range(5):
    print(i)

while idade < 30:
    idade += 1

# Listas
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
primeiro = numeros[0]

# Dicionários
pessoa = {"nome": "João", "idade": 25}
print(pessoa["nome"])

# Funções
def saudacao(nome):
    return f"Olá, {nome}!"

resultado = saudacao("Maria")