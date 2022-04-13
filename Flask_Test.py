import numpy as np
from flask import Flask, request, url_for, render_template
from functions import B_M_I_Status, convert_to_kg, convert_to_Metre

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods = ["POST"])
def calculate_BMI():
    BMI = round(convert_to_kg()/(convert_to_Metre()**2),2)
    BMI_health_status = B_M_I_Status(BMI)
    return render_template('home.html', BMI_health_status = BMI_health_status)

if __name__ == '__main__':
    app.run(debug=False)