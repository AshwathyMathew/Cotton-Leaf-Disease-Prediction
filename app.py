import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/',methods=['Get','Post'])
def home():
     return render_template('predict.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    msg=''
    output=""
    if request.method == 'POST':
        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(filename)
        from Leaf_Disease_Prediction import predict_disease
        disease, confidence = predict_disease(filename)
        if disease:
            output = f"Predicted Disease: {disease}, Confidence: {confidence:.2f}%"
            return render_template('Predict.html', msg=msg, output=output, Title="Disease Prediction")
    return render_template('Predict.html', msg=msg, output=output, Title="Disease Prediction")

if __name__ == "__main__":
    app.run(debug=True)

