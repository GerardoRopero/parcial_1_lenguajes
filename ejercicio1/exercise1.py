columns = ["kb","qb","kn","qn","kr","qr","k","q"]
pieces = ["p","k","q","b","n","r"]
numbers = "12345678"

def empieza_con(cadena, lista):
    for item in lista:
        if cadena.startswith(item):
            return item
    return None

def validar(cadena):

    i = 0

    # columna opcional
    col = empieza_con(cadena[i:], columns)
    if col:
        i += len(col)

    # pieza obligatoria
    if i < len(cadena) and cadena[i] in pieces:
        i += 1
    else:
        return False

    # acción
    if cadena[i:i+2] == "->":
        i += 2
    elif i < len(cadena) and cadena[i] == "X":
        i += 1
    else:
        return False

    # columna destino (obligatoria)
    col = empieza_con(cadena[i:], columns)
    if col:
        i += len(col)
    else:
        return False

    # número opcional
    if i < len(cadena) and cadena[i] in numbers:
        i += 1

    # debe terminar exactamente aquí
    return i == len(cadena)


# pruebas
tests = [
    "p->k4",
    "kbpXqn",
    "qXk7",
    "pXq",
    "b->kb2"
]

for t in tests:
    print(t, ":", validar(t))
