from flask import Flask, render_template, request,redirect, url_for
#render_template: collegare file HTML.
app = Flask(__name__)
#rotta principale
spesa = []
@app.route('/')
def home():
    return render_template('index.html')
#Fatto il posto di aggiungi
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        spesa.append(elemento)
        return redirect(url_for('home'))
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
