from flask import Flask, render_template, request
app = Flask(__name__)
import pickle

#open a file,where you store pickled data
file = open('model1.pk1', 'rb')

clf = pickle.load(file)
file.close()
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        Fever = int(myDict['Fever'])
        Age = int(myDict['Age'])
        Pain = int(myDict['Pain'])
        runnyNose= int(myDict['runnyNose'])
        DiffBreath = int(myDict['DiffBreath'])
        print(request.form)

        #Code for inference 
        inputFeatures = [Fever, Pain, Age, runnyNose, DiffBreath]
        infProb = clf.predict_proba([[100, 1, 22, -1, 1]])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100))
    return render_template('index.html')
    #return 'Hello World!' + str(infProb)

if __name__ == "__main__":
    app.run(debug=True)