from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/equipes')
def equipes():
    return render_template('equipes.html')

@app.route('/joueurs')
def joueurs():
    return render_template('joueurs.html')

@app.route('/histoire')
def histoire():
    return render_template('histoire.html')

@app.route('/resultats')
def resultats():
    return render_template('resultats.html')

@app.route('/equipe/dinamo-tbilissi')
def dinamo_tbilissi():
    return render_template('dinamo-tbilissi.html')

@app.route('/equipe/torpedo-koutaissi')
def torpedo_koutaissi():
    return render_template('torpedo-koutaissi.html')

@app.route('/equipe/gagra')
def gagra():
    return render_template('gagra.html')

@app.route('/equipe/dila-gori')
def dila_gori():
    return render_template('dila-gori.html')

@app.route('/iberia-1999')
def iberia_1999():
    return render_template('iberia-1999.html')

@app.route('/telavi')
def telavi():
    return render_template('telavi.html')

@app.route('/dinamo-batumi')
def dinamo_batumi():
    return render_template('dinamo-batumi.html')

@app.route('/samgurali')
def samgurali():
    return render_template('samgurali.html')

@app.route('/kolkheti-1913')
def kolkheti_1913():
    return render_template('kolkheti-1913.html')

@app.route('/sagarejo')
def sagarejo():
    return render_template('sagarejo.html')

if __name__ == '__main__':
    app.run(debug=True)
