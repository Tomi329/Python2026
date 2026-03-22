import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "entero",
    "cadena",
    "lista",
    ]
word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

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