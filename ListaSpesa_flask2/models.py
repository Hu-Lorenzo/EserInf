from flask_sqlalchemy import SQLAlchemy

# Inizializziamo SQLAlchemy
db = SQLAlchemy()

# Definiamo la classe del modello ListaSpesa
class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID unico per ogni elemento
    elemento = db.Column(db.String(100), nullable=False)  # Descrizione dell'elemento

    def __repr__(self):
        return f"<Elemento {self.elemento}>"
