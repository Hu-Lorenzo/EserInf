from flask import Flask, render_template, request, redirect, url_for

# Crea l'app Flask
app = Flask(__name__)

# Lista della spesa inizialmente vuota
spesa = []

# Rotta principale per visualizzare la lista
@app.route('/')
def home():
    return render_template('index.html', spesa=spesa)

# Rotta per aggiungere un elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        spesa.append(elemento)
    return redirect(url_for('home'))

# Rotta per rimuovere un elemento dalla lista, in base all'indice
@app.route('/rimuovi/<int:indice>', methods=['GET'])
def rimuovi(indice):
    if 0 <= indice < len(spesa):
        spesa.pop(indice)
    return redirect(url_for('home'))

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

