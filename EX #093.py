dict={} #MEU DICIONARIO 
lista_gols=[] #LISTA DE GOLS JOGADOR1
lista=[]
lista_partidas=[]
soma=cont=max=0
nome=''
while True:
    dict.clear()
    lista_gols.clear()
    soma=0
    dict['nome']=input('nome do jogador: ').title()
    partidas=int(input(f"quantas partidas {dict['nome']} jogou? "))
    lista_partidas.append(partidas)
    for i in range(0,partidas):
        lista_gols.append(int(input(f'quantos gols na {i+1}ª partida?')))
    for x in lista_gols:
        soma+=x
    dict['gols']=lista_gols[:]
    dict['total']=soma

    lista.append(dict.copy())
#OPÇÃO PARA BREAK
    opc=input('deseja continuar? ')
    if opc in 'Nn':
        break
print(lista)
#PRINT DOS DICIONARIOS
for dic in range(0,len(lista)):
    print(f'{'-='*30}\nJogador {dic+1}:{lista[dic]}\n{'-='*30}')

#VALORES DE CADA TITULO DO DICIONARIO
for i in range(0,len(lista)):
    for k,v in lista[i].items():
        print(f'\033[1;3{i+1}mo campo {k} tem valor {v}\033[m')

#COMPARAÇÃO DE CADA JOGADOR
for i in range(0,len(lista)):
    print(f'{'-='*30}\n\033[mo jogador {lista[i]['nome']} jogou {lista_partidas[i]} partidas.\033[1;3{i+1}m')
    for cont in range(0,len(lista[i]['gols'])):
        print(f'Na partida {cont+1}, fez {lista[i]['gols'][cont]} gols')

#FAZENDO A ARTILHARIA
print(f'{'-='*10}{'ARTILHARIA':^20}{'-='*10}')

cont+=1
for i in range(0,len(lista)):
    if i==0:
        max=lista[i]['total']
        nome=lista[i]['nome']
    if lista[i]['total']>max:
        max=lista[i]['total']
        nome=lista[i]['nome']
for i in range(0,len(lista)):
    for k,v in lista[i].items():
        if v==max:
            print(f'\033[33mo campeão é {nome} com {max} gols\033[m')

#EXERCICIO 95

while True:
    aproveitamento = input('mostrar dados de qual jogador? ').title().strip()
    for i in range(0,len(lista)):
        for k,v in lista[i].items():
            if v==aproveitamento:
                for x in range(0,len(lista[i]['gols'])):
                    print(f'\033[3{i+1}mno jogo {x+1} fez {lista[i]['gols'][x]}\033[m')

    if aproveitamento=='999':
        break

print(f'Nº  Nome{' '*10}    Total\n{'_'*25}')
for tabela in range(0,(len(lista))):
    print(f'{tabela+1} {lista[tabela]['nome']} {lista[tabela]['gols']}    {lista[tabela]['total']}')
    
    







