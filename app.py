from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle

app = Flask(__name__)
with open("random_forest_model.pickle", "rb") as f:
    model=pickle.load(f)



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=[ "GET","POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        status = request.form["stat"]

        cred_history = request.form["cred_history"]

        dur = int(request.form["dur"])

        savings = request.form['savings']

        prop = int(request.form["prop"])

        amou = int(request.form["amou"])

        emp_dur = int(request.form["emp_dur"])

        purp = int(request.form["purp"])

        age = int(request.form["age"])

        rate = int(request.form["rate"])

        prediction = model.predict([[status,cred_history,dur,savings,prop,amou,emp_dur,purp,age
                                     ,rate]])

        if prediction==0:
            output="Bad"
        else:
            output="Good"

        return render_template('home.html', prediction_text="{} client".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
