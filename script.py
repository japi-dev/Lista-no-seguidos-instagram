import json

# Ruta de los archivos
seguidos_archivo = '/content/following.json'
seguidores_archivo = '/content/followers_1.json'

# Abrimos archivo y lo almacenamos
seguidos = json.load(open(seguidos_archivo))['relationships_following']
seguidores = json.load(open(seguidores_archivo))

# Crear un diccionario para almacenar {usuario: href} para las personas que sigues
personas_que_sigo = {entry['value']: entry['href'] for item in seguidos for entry in item['string_list_data']}

# Crear un conjunto de personas que te siguen
personas_que_me_siguen = {entry['value'] for item in seguidores for entry in item['string_list_data']}

# Obtener las personas que sigues pero que no te siguen de vuelta
personas_que_no_me_siguen = personas_que_sigo.keys() - personas_que_me_siguen

# Imprimir las personas que no te siguen de vuelta junto con su enlace
print("Personas que no me siguen de vuelta:")
for user in personas_que_no_me_siguen:
    link = personas_que_sigo[user]
    print(f'Usuario: {user} - link: {link}')
