#solicita que o usuario coloque sua nota1 e sua nota2 e as mostrar para o usuario
nota1 = float(input('Primeira nota: '))
print('A sua primeira nota é:{}'.format(nota1))
nota2 = float(input('Segunda nota: '))
print('A seu segunda nota é:{}'.format(nota2))

#calcula a media do aluno e mostrarpra ele
media = (nota1 + nota2) / 2
print('A sua media é:{}'.format(media))

#exibe a media do aluno e fala se foi aprovado ou reprovado
if media >=6:
    print('Parabens, aluno aprovado!')
else:
    print('Poxa, aluno reprovado!')
