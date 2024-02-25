from flask import Flask, request, jsonify
from imgtotext import *

app = Flask(__name__)


# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/img2text', methods=['POST'])
def receive_data():
    data = request.json
    b64_string = data["img"]
    img2text = Img2Text(b64_string)
    imagen = img2text.base64aimg()
    imagen_procesada = img2text.procesar_imagen(imagen)
    imagen_mejorada = img2text.mejorar_calidad_letras(imagen_procesada)
    texto = img2text.imgatexto(imagen_mejorada)
    return jsonify({"texto": texto})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(port=6000,debug=True)  # Inicia el servidor en modo de depuración
