informacoes = {
    'Nome1':'Alan','Idade1': '15 anos','Cidade1':'São José dos Pinhais',
    'Nome2':'Ronaldo','Idade2': '54 anos','Cidade2':'Bugre',
    'Nome3':'Jucelina','Idade3':' 80 anos','Cidade3':'Balsa Nova',
}
informacoes.update({'Idade1':17})

informacoes.update({'Emprego1':'estudante' ,'Emprego2':'Pedreiro','Emprego3':'Aposentada'})

informacoes.pop('Idade1')

print(informacoes)
