from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle
import pandas as pd
#import scaler


#Flask 객체 인스턴스 생성
app = Flask(__name__)

model = pickle.load(open('sna.pkl', 'rb'))


#@app.route('/<int:num>')
@app.route('/')
def inputTest():
    return render_template('main.html')
    
@app.route('/boost',methods=['POST'])
def boost():
        age = request.form['a']
        EstimatedSalary = request.form['b']
        Female = request.form['c']
        Male = request.form['d']
        arr = pd.DataFrame([[age, EstimatedSalary, Female, Male]], columns= ['Age', 'EstimatedSalary','Female','Male'])
        #arr = np.array([[age, EstimatedSalary, Female, Male]])
        #arr[['Age', 'EstimatedSalary']] = scaler.fit_transform(arr[['Age', 'EstimatedSalary']])
        pred = int(model.predict(arr))
        #pred = model.boost(arr)
        #boost.predict(arr)
        return render_template('after.html', data=pred)

if __name__ == '__main__':
    app.run(debug=True)















#Flask 객체 인스턴스 생성
#app = Flask(__name__)

#@app.route('/') # 접속하는 url
#def index():
  #return render_template('main.html')

#if __name__=="__main__":
  #app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)