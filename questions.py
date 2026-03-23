import random

# cambiado lista --> diccionario
words = {
    "1": ["bucle", "lista"],
    "2": ["python", "entero", "cadena"],
    "3": ["programa", "variable", "funcion"]
    }
guessed = []
attempts = 6
puntaje = 0 # agregado

print("¡Bienvenido al Ahorcado!")
print()

# agregado
diff = (input("""Dificultades:
        1- Fácil
        2- Medio
        3- Difícil
              
Elija su dificultad: """))

while not diff.isnumeric() or diff < "1" or diff > "3":
        print("Entrada invalida")

        diff = (input("""Dificultades:
        1- Fácil
        2- Medio
        3- Difícil
                      
Elija su dificultad: """))
        
word = random.choice(words[diff])

while attempts > 0: 
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
                progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print(f"""¡Ganaste!
Puntaje obtenido: {puntaje}""")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    
    # agregado
    if not letter.isalpha() or len(letter) != 1:
        print("Entrada inválida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
        puntaje += 6 # agregado
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        puntaje -= 1 # agregado
        
    print()

else:
    puntaje = 0 # agregado
    print(f"""¡Perdiste! La palabra era: {word}
Puntaje obtenido: {puntaje}""")