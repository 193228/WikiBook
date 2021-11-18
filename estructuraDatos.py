import re

def creacionDataframe(lista):
    #print(lista['items'][0]['volumeInfo']['categories'])
    #print(lista['items'][0]["volumeInfo"]['title'])
    #print(lista['items'][0]['volumeInfo']['authors'])
    #print(lista['items'][0]['volumeInfo']['publisher'])
    #print(lista['items'][0]['volumeInfo']['publishedDate'])
    #print(lista['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
    #print(lista['items'][0]['volumeInfo']['language'])
    #print(lista['items'][0]['volumeInfo']['infoLink'])
    try:
        try:
            autores = lista['items'][0]['volumeInfo']['authors']
        except:
            autores = ["NA"]

        try:
            categorias = lista['items'][0]['volumeInfo']['categories']
        except:
            categorias = ["NA"]

        try:
            costoLibro = lista['items'][0]['saleInfo']['listPrice']['amount']
            tipoMoneda = lista['items'][0]['saleInfo']['listPrice']['currencyCode']
        except:
            costoLibro = "Sin Precio"
            tipoMoneda = ""

        try:
            rating = lista['items'][0]['volumeInfo']['averageRating']
            rating = int(rating)
        except:
            rating = 0

        try:
            numeroPaginas = lista['items'][0]['volumeInfo']['pageCount']
        except:
            numeroPaginas = "NA"

        try:
            preview = lista['items'][0]['volumeInfo']['previewLink']
            regex = "((978[\--–])?[0-9][0-9\--–]{10}[\--–][0-9xX])|((978)?[0-9]{9}[0-9Xx])"
            expresion = re.compile(regex)
            isbn = expresion.search(preview).group()
        except:
            isbn = ""

        try:
            publicacion = lista['items'][0]['volumeInfo']['publisher']
        except:
            publicacion = "NA"

        try:
            imagen = lista['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        except:
            try:
                imagen = lista['items'][1]['volumeInfo']['imageLinks']['thumbnail']
            except:
                imagen = "https://i0.wp.com/elfutbolito.mx/wp-content/uploads/2019/04/image-not-found.png?ssl=1"

        info = {
            "categoria": categorias,
            "tituloLibro": lista['items'][0]["volumeInfo"]['title'],
            "autores": autores,
            "publicacion": publicacion,
            "fechaPublicacion": lista['items'][0]['volumeInfo']['publishedDate'],
            "numeroPaginas": numeroPaginas,
            "rating": rating,
            "imagen": imagen,
            "lenguajeLibro": lista['items'][0]['volumeInfo']['language'],
            "informacionCompleta": lista['items'][0]['volumeInfo']['infoLink'],
            "Costo": costoLibro,
            "tipoMoneda": tipoMoneda,
            "Identificador": isbn
        }

        return info

    except:
        pass