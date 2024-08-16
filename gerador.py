import sumolib

# Carregar o arquivo .net.xml
net = sumolib.net.readNet('C:\bin\meu.net.xml')

# Abrir o arquivo .rou.xml para escrita
with open('C:\bin\meu.rou.xml', 'w') as routes_file:
    # Escrever a estrutura básica do arquivo
    routes_file.write('<routes>\n')

    # Exemplo de adição de veículos e rotas
    vehicle_id = 0
    for edge in net.getEdges():
        # Aqui, você pode definir as rotas específicas para as edges da rede
        routes_file.write(f'    <vehicle id="vehicle_{vehicle_id}" type="car" route="edge_{edge.getID()}"/>\n')
        vehicle_id += 1

    # Fechar a estrutura do arquivo
    routes_file.write('</routes>\n')

print(f'Arquivo .rou.xml gerado com sucesso em: C:\bin\meu.rou.xml')
