from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    prenom = request.form['prenom']
    adresse = request.form['adresse']
    tel= request.form['tel']
    gmail= request.form['gmail']
    carte= request.form['carte']
    bank = request.form['bank']

    

    return f"<h1>Merci {nom} !</h1><p>Nous avons bien reçu votre message.</p>"

