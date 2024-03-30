from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from the POST request
    feature1 = request.json['feature1']
    feature2 = request.json['feature2']

    # Perform prediction using the machine learning model
    # Replace this code with your actual prediction logic
    prediction = predict_model(feature1, feature2)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

def predict_model(feature1, feature2):
    # Replace this function with your actual model prediction logic
    # Example: return model.predict([[feature1, feature2]])
    return 'Dummy Prediction'

if __name__ == '__main__':
    app.run(debug=True)
