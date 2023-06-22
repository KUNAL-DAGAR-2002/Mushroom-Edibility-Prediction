from flask import Flask,request,render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle as pkl 

app = Flask(__name__)

scaler = pkl.load(open('models/scaler.pkl','rb'))
model = pkl.load(open('models/model.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    
    if request.method == 'POST':
        features = ['cap_shape','cap_surface','cap_color','bruises','odor','gill_attachment','gill_spacing','gill_size','gill_color','stalk_shape','stalk_root','stalk_surface_above_ring','stalk_surface_below_ring','stalk_color_above_ring','stalk_color_below_ring','ring_number','ring_type','spore_print_color','population','habitat']

        data = []

        for i in features:
            data.append(int(request.form.get(i)))
        data = scaler.transform([data])

        result = model.predict(data)
        result = round(result[0])
        if result==0:
            return render_template('index.html',result = 'Eatable')
        else:
            return render_template('index.html',result = 'Not Eatable')
        
        
        
        # return data[0]
    else:
        return render_template('index.html')

       


if __name__=="__main__":
    app.run(debug=True)