from flask import Flask,render_template,redirect,url_for,request
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def question():
    if request.method == 'POST':
        ques = request.form['msg']

        data = np.array([[ques]])
        input_data_as_numpy_array = np.asarray(data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        loaded_model=pickle.load(open('C:/Users/hp/Downloads/FLASK/trained_model.sav','rb'))

        my_prediction=loaded_model.predict(input_data_reshaped)
        return render_template('diab_result.html', prediction=my_prediction)

app.run(debug=True)
