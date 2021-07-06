distancia = float(input('\033[34mQual é a distância da sua viagem? '))
print(f'\033[34mVocê está prestes a começar uma viagem de \033[32m{distancia}Km')

# if distância <= 200:
#   preço = distância * 0.50
# else:
#   preço = distância * 0.45

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'\033[34mE preço da passagem será de \033[32mR${preco:.2f}.')
