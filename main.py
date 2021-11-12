import threading

import pandas as pd
from flask import Flask, render_template, request, flash
from concurrency import *
from isbn import *
from estructuraDatos import *
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
diccionario = []
consulta = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leer', methods=['POST'])
def leerTxt():
    diccionario.clear(); consulta.clear();
    if request.method == 'POST':
        file = request.files['file']
        lineas = file.stream.read().decode("utf-8")
        listaIsbn = obtenerIsbn(lineas)
        if len(listaIsbn)>0:
            listaLibros = asyncio.run(main(listaIsbn))
            consulta.append(listaLibros[2])
            for i in listaLibros[0]:
                x = creacionDataframe(i)
                if x is not None:
                    diccionario.append(x)
            dataframeInfo = pd.DataFrame(diccionario)
            print(dataframeInfo)
            if dataframeInfo.empty:
                flash("No se leyo nigun ISBN O la api no lo reconoce O solicitud excedida por hoy")
                return render_template('index.html')
            else:
                flash("Tiempo Transcurrido Usando Concurrencia y asyncrono: "+str(listaLibros[1])+" Segundos, "+"Numero de solicitudes tomadas: "+str(len(listaIsbn))+" Cantidad de ISBN Validos: "+str(len(diccionario))+" Esto debido a la cuota permitida de google api o libro no se encuentra en la api")
                return render_template('app.html', column_names = dataframeInfo.columns.values, row_data = list(dataframeInfo.values.tolist()))
        else:
            flash("No se leyo nigun ISBN O la api no lo reconoce O solicitud excedida por hoy")
            return render_template('index.html')
    else:
        return 'Error'

@app.route('/eleccion', methods=['POST'])
def opciones():
    dato = request.form.get('opciones')
    df = pd.DataFrame(diccionario)

    if dato == "fechaPublicacion":
        dataframe = df.sort_values(by='fechaPublicacion', ascending=True)

    if dato == "tituloLibro":
        dataframe = df.sort_values(by='tituloLibro', ascending=True)

    if dato == "categoria":
        dataframe = df.sort_values(by='categoria', ascending=True)

    if dato == "autores":
        dataframe = df.sort_values(by='autores', ascending=True)

    if dato == "idioma":
        dataframe = df.sort_values(by='lenguajeLibro', ascending=True)

    if dato == "rating":
        dataframe = df.sort_values(by='rating', ascending=False)

    return render_template('app.html', column_names = dataframe.columns.values, row_data = list(dataframe.values.tolist()))

@app.route('/viewConsulta', methods=['POST'])
def consultas():
    x = "&key="
    newList = []
    for i in range(len(consulta[0])):
        extraer = consulta[0][i].find(x)
        res = consulta[0][i][:extraer]
        newList.append(res)

    dataframe = pd.DataFrame({
        "Peticiones Realizadas":newList
    })
    return render_template("tablaRequest.html", tables=[dataframe.to_html(classes='data')], titles=dataframe.columns.values)

if __name__ == '__main__':
    app.run()
    #threading.Thread(target=lambda: app.run(port=3000, debug=True, use_reloader=False)).start()