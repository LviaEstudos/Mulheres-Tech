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