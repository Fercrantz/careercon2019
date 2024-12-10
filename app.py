from flask import Flask, request, jsonify
import joblib
import numpy as np

# Criando a aplicação Flask
app = Flask(__name__)

# Carregando o modelo, scaler e label encoder
model_gb = joblib.load('model_gb.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Endpoint para predição
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebe os dados no formato JSON
        data = request.get_json()

        # Extrai as features (esperando que as features estejam em uma lista dentro do JSON)
        features = np.array(data['features']).reshape(1, -1)

        # Normalizando as features com o scaler carregado
        features_scaled = scaler.transform(features)

        # Fazendo a predição
        prediction = model_gb.predict(features_scaled)

        # Decodificando a previsão de volta para a categoria original
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        # Retornando a resposta como JSON
        return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
