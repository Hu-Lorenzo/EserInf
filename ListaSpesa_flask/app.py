from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, ListaSpesa  # Importa db e ListaSpesa dal file models

app = Flask(__name__)
# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  # Percorso del database SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabilita il tracking delle modifiche

# Inizializza SQLAlchemy con l'app
db.init_app(app)

# Crea il database (se non esiste) all'avvio dell'app
with app.app_context():
    db.create_all()

# Rotta principale per visualizzare la lista della spesa
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()  # Ottieni tutti gli elementi
    return render_template('index.html', lista=lista_spesa)

# Rotta per aggiungere un elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form.get('elemento') 
    if elemento:  
        nuovo_elemento = ListaSpesa(elemento=elemento)  # Crea un nuovo elemento
        db.session.add(nuovo_elemento)  # Aggiungi il nuovo elemento alla sessione
        db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

# Rotta per rimuovere un elemento dalla lista
@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento = ListaSpesa.query.get_or_404(id)  # Trova l'elemento per ID, restituisce errore 404 se non trovato
    db.session.delete(elemento)  # Elimina l'elemento
    db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

# Rotta per svuotare tutta la lista
@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete()  # Elimina tutti gli elementi nella tabella
    db.session.commit()  # Salva i cambiamenti nel database
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
