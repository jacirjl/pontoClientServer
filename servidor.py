from flask import Flask, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_image():
    # Recebe a imagem codificada em base64
    data = request.get_json()
    image_data = data['image']

    # Decodifica a imagem de base64 para um formato que o OpenCV possa ler
    img_data = base64.b64decode(image_data)
    np_img = np.frombuffer(img_data, dtype=np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Aqui você pode salvar a imagem ou fazer algum processamento com ela
    cv2.imwrite('received_image.jpg', img)

    return jsonify({"message": "Imagem recebida e salva com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
