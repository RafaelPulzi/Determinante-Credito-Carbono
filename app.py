import flask

app = flask.Flask(__name__)

if(__name__ == '__main__'):
    app.run(debug=True)

@app.route('/')
def home():
    return "Ola mundo"

@app.route('/comArvores')
def home():
    return render_template('comArvores.html')

@app.route('/semArvores')
def home():
    return render_template('semArvores.html')