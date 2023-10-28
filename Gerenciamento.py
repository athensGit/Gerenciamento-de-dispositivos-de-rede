rede = []
def add_dispositivo(nome, ip):
  dispositivo = {'Nome': nome,
                 'IP': ip}
  rede.append(dispositivo)
  print('Dispositivo cadastrado!!')
def listar_dispositivos():
  if len(rede) == 0:
    print('Não há dispositivos.')
  else:
    for dispositivo in rede:
      print(dispositivo['Nome'],':', dispositivo['IP'])
def buscar_dispositivo(nome):
  encontrou = False
  for dispositivo in rede:
    if nome == dispositivo['Nome']:
      print(dispositivo['Nome'], ':', dispositivo['IP'])
      encontrou = True
      break
  if not encontrou:
    print('Objeto não encontrado')
def remover_dispositivo(nome):
  encontrou = False
  for dispositivo in rede:
    if nome == dispositivo['Nome']:
      rede.remove(dispositivo)
      print('Dispositivo removido')
      encontrou = True
      break
  if not encontrou:
    print('Dispositivo não encontrado')
while True:
  print('------Menu------')
  print('1 - Adicionar dispositivo')
  print('2 - Listar dispositivos')
  print('3 - Buscar dispositivos')
  print('4 - Remover um dispositivo')
  print('0 - Sair')
  opcao = input ('Digite o número da sua opção:')
  if opcao == '1':
    nome = input('Digite o nome:')
    ip = input('Digite o IP:')
    add_dispositivo(nome, ip)
  elif opcao == '2':
    listar_dispositivos()
  elif opcao == '3':
    nome = input('Digite o nome:')
    buscar_dispositivo(nome)
  elif opcao == '4':
    nome = input('Digite o nome:')
    remover_dispositivo(nome)
  elif opcao == '0':
    break
  else:
    print('Opção inválida!')
