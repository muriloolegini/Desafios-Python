from datetime import datetime
import instaloader

# Carrega a lib e faz login com a conta desejada #
L = instaloader.Instaloader()
L.login('muriloolegini', 'Inst@*2023')

# Carrega os dados de seguidores e seguindo do perfil escolhido #
followers = instaloader.Profile.from_username(L.context, "muriloolegini").get_followers()
followees = instaloader.Profile.from_username(L.context, "muriloolegini").get_followees()

# Mostra resultados #
print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees._data['count']))
print('\n')
print('Lista e informações de seguidores:')
print('\n')
print(followers._data['edges'])