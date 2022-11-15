from flask import Flask, flash, request, redirect, url_for, render_template
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

model = load_model('nutrition.h5')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home_html.html')


@app.route('/bmi', methods=['get'])
def bmi():
    return render_template('bmi_html.html')


@app.route('/pred', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
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
        flash('Image successfully uploaded and displayed below')

        img = image.load_img(filepath, target_size=(64, 64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        pred = np.argmax(model.predict(x), axis=1)
        foods = ['Apple', 'Banana', 'Bhel puri', 'Burger', 'Egg', 'Mango', 'Onion', 'Pizza']
        text = str(foods[pred[0]])
        print(text)

        def apple_nut():
            name = "The Food displayed here is Apple"
            info = '''Apples are considered nutrient-dense fruits, meaning they provide a lot of nutrients per serving.
                    One medium 7-ounce (200-grams) apple offers the following nutrients '''
            a = "Calories: 104"
            b = "Carbs: 28 grams"
            c = "Fiber: 5 grams"
            d = "Vitamin C: 10% of the Daily Value (DV)"
            e = "Copper: 6% of the DV"
            f = "Potassium: 5% of the DV"
            g = "Vitamin K: 4% of the DV"
            return [name, info, a, b, c, d, e, f, g]

        def banana_nut():
            name = "The Food displayed here is Banana"
            info = '''Bananas contain a fair amount of fiber and several antioxidants.
                    One regular-sized banana (126 grams) contains: '''
            a = "Calories: 112"
            b = "Carbs: 29 grams"
            c = "Fiber: 3 grams"
            d = "Vitamin C: 12% of the Daily Value (DV)"
            e = "Copper: 11% of the DV"
            f = "Potassium: 10% of the DV"
            g = "Protein: 1 gram"
            return [name, info, a, b, c, d, e, f, g]

        def bhelpuri_nut():
            name = "The Food displayed here is Bhel Puri"
            info = '''Bhelpuri is a savoury snack originating from India, and is also a type of chaat.
                    One serving of Bhel Puri provides the following nutrients: '''
            a = "Calories: 185"
            b = "Carbs: 3 grams"
            c = "Cholesterol: 0.0 mg"
            d = "Fat: 1.5 grams"
            e = "Vitamin c: 12.6 % of the DV"
            f = "Potassium: 173.3 mg"
            g = "Protein: 10 grams"
            return [name, info, a, b, c, d, e, f, g]

        def burger_nut():
            name = "The Food displayed here is Burger"
            info = '''Burgers or hamburgers as they are also called are a type of fast food.
                    one 100 grams of chicken burger contains the following nutrients:'''
            a = "Calories: 266"
            b = "Carbs: 30.3 grams"
            c = "Fiber: 1.1 grams"
            d = "Fat: 10.1 grams"
            e = "Sugars: 5.2 grams"
            f = "Sodium: 396 mg"
            g = "Protein: 13.3 grams"
            return [name, info, a, b, c, d, e, f, g]

        def egg_nut():
            name = "The Food displayed here is Eggs"
            info = '''Eggs are among the most nutritious foods on the planet.
                    A whole egg contains all the nutrients required to turn a single cell into a baby chicken.
                    A single large boiled egg contains:'''
            a = "Vitamin A: 6% of the RDA"
            b = "Folate: 5% of the RDA"
            c = "Vitamin B5: 7% of the RDA"
            d = "Vitamin B12: 9% of the RDA"
            e = "Vitamin B2: 15% of the RDA"
            f = "Phosphorus: 9% of the RDA"
            g = "Selenium: 22% of the RDA"
            return [name, info, a, b, c, d, e, f, g]

        def mango_nut():
            name = "The Food displayed here is Mango"
            info = '''Many people love mango — not only because it is delicious but also because it is very nutritious.
                    One cup (165 grams) of fresh mango provides:'''
            a = "Calories: 99"
            b = "Protein: 1.4 grams"
            c = "Carbs: 24.7 grams"
            d = "Fat: 0.6 grams"
            e = "Fiber: 2.6 grams"
            f = "Sugar: 22.5 grams"
            g = "Vitamin C: 67% of the Daily Value (DV)"
            return [name, info, a, b, c, d, e, f, g]

        def onion_nut():
            name = "The Food displayed here is Onion"
            info = '''Raw onions are very low in calories, with only 40 calories per 3.5 ounces (100 grams).
                    By fresh weight, they are 89% water, 9% carbs, and 1.7% fiber, with tiny amounts of protein and fat.
                    The main nutrients in 3.5 ounces (100 grams) of raw onions are:'''
            a = "Calories: 40"
            b = "Protein: 1.1 grams"
            c = "Carbs: 9.3 grams"
            d = "Fat: 0.1 grams"
            e = "Fiber: 1.7 grams"
            f = "Sugar: 4.2 grams"
            g = "Water: 89%"
            return [name, info, a, b, c, d, e, f, g]

        def pizza_nut():
            name = "The Food displayed here is Pizza"
            info = '''Pizza sold in fast-food restaurants and convenience stores is among the unhealthiest of choices.
                    It tends to be the highest in calories, unhealthy fats, carbs and sodium.
                    One large slice (167 grams) of Pizza Hut Pepperoni Lovers Pizza provides:'''
            a = "Calories: 460"
            b = "Carbs: 37 grams"
            c = "Fat: 26 grams"
            d = "Sugar: 1 gram"
            e = "Sodium: 900 mg — 38% of the RDI"
            f = "Protein: 12.2grams"
            g = "So, eating just pizza every day is not a healthy, sustainable diet"
            return [name, info, a, b, c, d, e, f, g]

        if text == 'Apple':
            nutrient = apple_nut()
        elif text == 'Banana':
            nutrient = banana_nut()
        elif text == 'Bhel puri':
            nutrient = bhelpuri_nut()
        elif text == 'Burger':
            nutrient = burger_nut()
        elif text == 'Egg':
            nutrient = egg_nut()
        elif text == 'Mango':
            nutrient = mango_nut()
        elif text == 'Onion':
            nutrient = onion_nut()
        elif text == 'Pizza':
            nutrient = pizza_nut()
        return render_template('index.html', filename='uploads_images/'+ filename, name=nutrient[0], info=nutrient[1], a=nutrient[2],
                               b=nutrient[3], c=nutrient[4], d=nutrient[5], e=nutrient[6], f=nutrient[7], g=nutrient[8])
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads_images/' + filename), code=301)


if __name__ == "__main__":
    app.run()

