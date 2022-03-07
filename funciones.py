import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra = []
    for letraIndex in range(0, len(alfabeto)):
      if letra.lower() == alfabeto[letraIndex].lower():
          #letra=alfabeto[letraIndex-1].lower()
          letra = letraIndex-1

    print("letra",letra)
    # hay que declarar la variable fuera sino si hay mas de un resultado solo devolvera el ultimo
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            for letraIndex in range(0, len(alfabeto)):
              # no me da tiempo, en este if debemos comprobar que palabra[0] == bucle sobre el string alfabeto hasta <= letra
              if palabra[0].lower() == letra.lower():
                # si no esta en la lista añado la palabra 
                if palabra not in resultado:
                  resultado.append(palabra)
    print("resultado",resultado)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    clients_list[nif] = {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    cartas_copy=cartas_iniciales
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            print(cartas_aleatorias)
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            if(len(cartas_aleatorias)==0):
              cartas_aleatorias.remove(carta)

    return combinaciones

    
