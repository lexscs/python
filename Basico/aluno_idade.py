'''Vamos fazer um peça três idades dos aluno de, e em seguida calcule a media de idade dos alunos, e classifique a sala como jovem criança, etc'''

idade1 = int(input('\nDigite a idade do aluno nº1: '))
idade2 = int(input('\nDigite a idade do aluno nº2: '))
idade3 = int(input('\nDigite a idade do aluno nº3: '))
media = (idade1 + idade2 + idade3) / 3

print('\n')

if media > 40:
    print('Pertence a turma acima de 40 anos')
elif media < 25:
    print('Pertence a turma jovem abaixo de 25 anos')
else:
    print('Pertence a turma adulta')