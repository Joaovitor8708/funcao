def estoque(nome, quantidade, valor):
    estoque = quantidade*valor
    return estoque

def calculo(nota1, nota2):
    soma = nota1 + nota2
    media = soma/2
    return media
def mostrar_resultado(media, nome):
    if media >= 7:
        return nome, 'aprovado'
    elif media >= 4:
        return nome, 'recuperação'
    elif media <= 4:
        return nome, 'reprovado'

def argumento(num1):
    if num1 > 0:
        return 'P'
    elif num1 < 0:
        return 'N'
    else:
        return 'Z'

def adicao(numeros):
    cont = 0
    for x in numeros:
        cont += x
    return cont