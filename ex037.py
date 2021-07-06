# Condições Aninhadas

nome = str(input('Qual é o seu nome? ')).strip()
if nome[:8].lower() == 'thayanne':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro':
    print('O seu nome é muito popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
print(f'Tenha um bom dia, {nome.capitalize()}!')
