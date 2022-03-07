from ctypes import sizeof
import random
import re


def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    list_words = []
    
    f = open(filename, mode="rt", encoding="utf-8")


    linea = f.readline()
    while linea != "":
        list_words.append(linea.upper()[0]+linea.upper()[1]+linea.upper()[2]+linea.upper()[3]+linea.upper()[4])
        linea = f.readline()

    f.close()
    

    random_number = random.randint(0, len(list_words)-1)
    return list_words[random_number]

def compare_words(word,secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position=[]
    same_letter=[]

    for i in range(0, len(word)):
      if word[i]==secret[i]:
        same_position.append(i)
      else:
        for e in range(0, len(word)):
          if word[i]==secret[e]:
            same_letter.append(i)
    print(same_position)
    print(same_letter)
    return same_position,same_letter


def print_word(word,same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ["-","-","-","-","-"]

    for e in (same_letter):
      transformed[e]=word[e]
      
    for i in (same_letter_position):
      transformed[i]=word[i].lower()
      
    return transformed[0]+transformed[1]+transformed[2]+transformed[3]+transformed[4]
            

def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    list_words = []
    
    f = open(filename, mode="rt", encoding="utf-8")


    linea = f.readline()
    while linea != "":
        if re.match('^[a-zA-Z_]+$', linea):
          if linea[4] == "\n":
            list_words.append(linea.upper()[0]+linea.upper()[1]+linea.upper()[2]+linea.upper()[3]+linea.upper()[4])          
        linea = f.readline()

    f.close()

    random_number = random.randint(0, len(list_words)-1)
    return list_words[random_number]

def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    x=0
    wordMatching=""
    while x!=1:
      word = input("Introduce una nueva palabra(checkValidWord): ")
      for selectedWord in (selected):
        if selectedWord==word:
          wordMatching=word
          x=1
    return wordMatching

if __name__ == "__main__":
    #check_valid_word(["CASA","CALLE"])
    secret2 = choose_secret_advanced('palabras_extended.txt')

    secret = choose_secret('palabras_reduced.txt')
    # Debug: esto es para que sepas la palabra que debes adivinar
    print("Palabra a adivinar: "+secret)
    for repeticiones in range(0, 6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word.upper(),secret)
        resultado = print_word(word.upper(),same_letter,same_position)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)
