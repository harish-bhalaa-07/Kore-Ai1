import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('modelamount.pkl','rb'))


@app.route('/')
def home():
    return render_template('index1.html')  #html page here


@app.route('/predict',methods=['POST'])
def predict():
    
    int_features=[[int(x) for x in request.form.values()]]
    print(int_features)
    final_features=np.array(int_features)  
    prediction=model.predict(final_features)
    
    output=prediction
    
    return render_template('index1.html',prediction_text='Loan amoun tis {}'.format(output))



if __name__=="__main__":
    app.run(debug=True)