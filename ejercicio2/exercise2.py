def es_letra(c):
    return c.isalpha()

def es_letra_o_numero(c):
    return c.isalnum()

def afd_id(cadena):
    estado = "q0"

    for c in cadena:
        if estado == "q0":
            if es_letra(c):
                estado = "q1"
            else:
                return "NO ACEPTA"
        
        elif estado == "q1":
            if es_letra_o_numero(c):
                estado = "q1"
            else:
                return "NO ACEPTA"

    if estado == "q1":
        return "ACEPTA"
    else:
        return "NO ACEPTA"


# Pruebas
pruebas = ["A1", "variable9", "Z", "9abc", "_test"]

for p in pruebas:
    print(p, "->", afd_id(p))
