from flask import Flask ,render_template,request
import pickle
import numpy as np




app =Flask(__name__)
def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


@app.route('/', methods=['POST','GET'])

def index():

    if request.method == 'POST':
        
        
       
  
        feature_list =[[8, 1.3, 1,1,1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,0,0,1,0,1,0,0]]

        
        
        prediction(feature_list)
        

        
        

        print(pred)


    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)