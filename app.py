from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from model import scrape_info

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template
@app.route("/")
def home():

    # Return template and data
    return render_template("index.html")

# Route to render index.html template
@app.route("/Neural")
def network():

    # Return template and data
    return render_template("DeepLearn.html")

# Route to render index.html template
@app.route("/Forest")
def forest():

    # Return template and data
    return render_template("RandomForest.html")

# Route to render index.html template
@app.route("/SVM")
def svm():

    # Return template and data
    return render_template("svmModel.html")

# Route to render index.html template
@app.route("/transport")
def trans():

    # Return template and data
    return render_template("transportStock.html")

# Route to render index.html template
@app.route("/Word")
def word():

    # Return template and data
    return render_template("tf_idf.html")

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    df = scrape_info()
    
    redirect('/scrape')
    return render_template("Bayes.html", outcome=df['outcome'].iloc[0], stock=df['stock'].iloc[0])

# Route to render index.html template
@app.route("/bayes")
def bayes():
       
     # Return template and data
    return render_template("Bayes.html", outcome="", stock=""  )

if __name__ == "__main__":
    app.run(debug=True)