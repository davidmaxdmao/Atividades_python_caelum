#Qeustão 1
#Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 8, 3, 3, -52]



lista = [12,-2, 4, 8, 29, 45, 78, 36, -17, 2, 8, 3, 3, -52]

# a) imprima o maior elemento

print('Questão a): {}'.format(max(lista)))

# b) imprima o menor elemento
print('Questão b): {}'.format(min(lista)))

#c) imprima os números pares
print('Questão c: ')
for num in lista:
    if num % 2 == 0:
        print(' número pá: {}'.format(num))

#d)imprima o número de ocorrências do primeiro elemento da lista
print('Questão c: {}'.format(lista.count(lista[0])))

#e)imprima a média dos elementos
cont = 0
aux = 0

for num in lista:
    aux = aux + num
    cont += 1
media = aux / cont

print('Questão e: {:.2f}'.format(media))

#f)imprima a soma dos elementos de valor negativo
negativo = 0
for num in lista:
    if num < 0:
        negativo += num
print('Questão f: {}'.format(negativo))