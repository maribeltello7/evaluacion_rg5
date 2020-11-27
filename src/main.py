from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def csv_como_json():
    lista_items = convertir_csv_a_json()
    return jsonify(lista_items)

def convertir_csv_a_json():
    ruta_archivo = 'data/employees.csv'
    lista = []
    with open(ruta_archivo) as archivo_csv:
        lector_diccionario = csv.DictReader(archivo_csv)
        for mapa in lector_diccionario:
            lista.append(mapa)
        return lista

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")