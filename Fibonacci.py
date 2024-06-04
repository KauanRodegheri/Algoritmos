#FIBONACCI
lista=[0,1]
cont=0
termo=''

while cont<=10:
    cont+=1
    lista.append(lista[-2]+lista[-1])

print(lista)

while cont>=10 and termo!='N':
    termo=int(input('deseja mais quantos termos?'))
    cont+=1
    for i in range(termo):
        lista.append(lista[-2]+lista[-1])
    print(lista)

