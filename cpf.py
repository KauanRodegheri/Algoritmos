
cpfV=(input('cpf: '))
soma=0
    #RETIRANDO OS 2 DIGITOS SE 
def cpff(n):  
    n1=cpfV[0:9]
    soma=0

        #DESCOBRINDO O 1º DIGITO
    for i in range(0,9):
        cpf=int(n1[i])*(10-i)
        soma+=cpf
    cpf=soma%11
        #REGRAS DO CPF (1 OU 0 == 0 )
    if cpf==0 or cpf==1:
        cpf=0
    else:
        cpf=11-cpf
        #DESCOBRINDO 2° DIGITO
    n2=n1+(str(cpf))
    soma=0 
    for i in range (0,10):
        cpf=int(n2[i])*(11-i)
        soma+=cpf
    cpf=soma%11
    cpf=11-cpf
    n3=n2+(str(cpf))
        #VALIDAÇÃO
    if n3==n:
        print('cpf validado')
    elif n3!=n:
        print(f'cpf invalido, numero correto: {n3}')

cpff(cpfV)

cpfV=input('digite o seu cpf')
cpff(cpfV)







