from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        yr_built = int(request.form['yr_built'])
        yr_renovated=int(request.form['yr_renovated'])
        sqft_living=int(request.form['sqft_living'])
        sqft_lot=int(request.form['sqft_lot'])
#
#        Seller_Type_Individual=request.form['Seller_Type_Individual']
#        if(Seller_Type_Individual=='Individual'):
#            Seller_Type_Individual=1
#        else:
#            Seller_Type_Individual=0	
#        Transmission_Mannual=request.form['Transmission_Mannual']
#        if(Transmission_Mannual=='Mannual'):
#            Transmission_Mannual=1
#        else:
#            Transmission_Mannual=0

        prediction=model.predict([[yr_built, yr_renovated, sqft_living, sqft_lot]])
        output=round(prediction[0],2)
 #       if output<0:
 #           return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
 #       else:
        return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)