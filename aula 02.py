# Código para liberar acesso para maiores de 18 anos

'''print('Qual a sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERAD! BOA FESTA!')
else:
    print('ACESSO NEGADO! VOCÊ É MENOR DE IDADE')'''

# Código para liberar acesso para miores de 19 anos

'''print('Qual a sua idade?')
idade = int(input())

if idade < 18:
    print('ACESSO NEGADO')
elif idade == 18:
    print('VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁ ACESSO')
else:
    print('ACESSO LIBERADO! BOA FESTA!')'''

# Código para verificar se o aluno está aprovado

'''print('Digite a média do 1º bimestre')
M1 = float(input())
print('Digite a média do 2º bimestre')
M2 = float(input())
print('Digite a média do 3º bimestre')
M3 = float(input())
print('Digite a média do 4º bimestre')
M4 = float(input())
media = (M1 + M2 + M3 + M4) / 4
print('A média do aluno é', media)

if media >= 7:
    print('APROVADO')
elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')'''

# Código para verificar se pode participar do Mulheres Tech

'''print ('Qual seu gênero? (F OU M)')
genero = input().upper()
print('Qual município você mora?')
municipio = input().lower()

if genero == 'F' and municipio == 'rio de janeiro':
    print('PARABÉNS! VOCÊ PODE PARTICIPAR DO MULHERES TECH')
else:
    print('VOCÊ NÃO PODE PARTICIPAR DO MULHERES TECH')'''

# Código para liberar acesso de um filme para maiores de 18 e 16 ou mais acompanhados dos responsáveis

print('BEM VINDO AO CINEMA SEVERIANO RIBEIRO')
print (' ')
print('Qual a sua idade?')
idade = int(input())

if idade >= 18:
    print('ACESSO LIBERADO!\nBOM FILME!')

elif idade >= 16:
    print('O FILME SELECIONADO É PARA MAIORES DE 18 ANOS\nPARA ASSISTIR PRECISA ESTAR COM O RESPONSÁVEL\nESTÁ ACOMPANHADO DO RESPONSÁVEL?')
    resposta = input().upper()
    if resposta == 'SIM':
        print('ACESSO LIBERADO\nBOM FILME!')
    else:
        print('VOCÊ SÓ PODE VER O FILME COM UM RESPONSÁVEL\nESCOLHA OUTRO FILME!')

else:
    print('ESTE FILME É PARA MAIORES DE 18 ANOS\nESCOLHA OUTRO FILME!')