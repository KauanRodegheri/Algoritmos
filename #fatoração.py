import numpy
fat=int(input('digite o numero a ser fatorado: '))
cont=0
lista=[fat]

while cont!=fat-1:
    cont+=1
    lista.append(lista[-1]-1)
print(f'{fat}! = {lista} = {numpy.prod(lista)}')

while cont>=fat-1:
    termo=int(input('deseja qual termo agora? '))
    lista=[termo]
    cont+=1
    for i in range(termo-1):
        lista.append(lista[-1]-1)
    print(f'{termo}! = {lista} = {numpy.prod(lista)}')
    
