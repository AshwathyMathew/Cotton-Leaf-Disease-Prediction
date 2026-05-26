import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Create a folder to store uploaded images
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('predict.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    msg = ''
    image_url = None  # Variable to store the image path

    if request.method == 'POST':
        if 'image' not in request.files:
            msg = "No file part in the request."
            return render_template('predict.html', msg=msg, Title="Disease Prediction")
        
        image = request.files['image']
        if image.filename == '':
            msg = "No file selected for uploading."
            return render_template('predict.html', msg=msg, Title="Disease Prediction")
        
        # Save the uploaded image
        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        image_url = filepath  # Path to the uploaded image

        # Import the prediction function and make predictions
        from Leaf_Disease_Prediction import predict_disease
        disease, confidence = predict_disease(filepath)
        if disease:
            # Render the relevant HTML page based on the predicted disease
            disease_page = f"{disease.lower()}.html"
            return render_template(disease_page, confidence=confidence, image_url=image_url)
    
    return render_template('predict.html', msg=msg, Title="Disease Prediction")

if __name__ == "__main__":
    app.run(debug=True, port=5001)