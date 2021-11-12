import re

def obtenerIsbn(cadena):
    lista = []
    regex = "((978[\--–])?[0-9][0-9\--–]{10}[\--–][0-9xX])|((978)?[0-9]{9}[0-9Xx])"
    expresion = re.compile(regex)
    id = expresion.findall(cadena)

    for i in id:
        for j in i:
            if len(j) > 5:
                lista.append(j)

    return lista