from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads_images/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

model = load_model('Nutrition.h5')


@app.route('/')
def home():
    return render_template('home_html.html')


@app.route('/bmi', methods=['get'])
def bmi():
    return render_template('bmi_html.html')


@app.route('/pred', methods=['get'])
def index():
    return render_template('indexduplicate.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/classifydup', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')

        img = image.load_img(filepath, target_size=(64, 64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        pred = np.argmax(model.predict(x), axis=1)
        foods = ['Apple', 'Banana', 'Bhel puri', 'Burger', 'Egg', 'Mango', 'Onion', 'Pizza']
        print(foods[pred[0]])
        apple = '''
                Nutients: 500
                Fat: 0
                Calories: 100
        '''
        pizza = '''     Pizza
                        Nutients: 0
                        Fat: 500
                        Calories: 200
                '''
        banan = '''
                                Nutients: 5150 \n
                                Fat: 100 \n
                                Calories: 2000
                        '''
        text = str(foods[pred[0]])
        print(text)
        if text == 'apple':
            return render_template('indexduplicate.html', filename='uploads_images/' + filename, imgg=apple)
        elif text == 'pizza':
            return render_template('indexduplicatehtml', filename='uploads_images/' + filename, imgg=pizza)
        else:
            return render_template('indexduplicate.html', filename='uploads_images/' + filename, imgg=banan)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


# @app.route('/display/<filename>')
# def display_image(filename):
#     return redirect(url_for('static', filename='uploads_images/' + filename), code=301)


if __name__ == "__main__":
    app.run()