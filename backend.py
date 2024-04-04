from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manual-character-creation')
def manual_character_creation():
    return render_template('character_creation.html')

if __name__ == '__main__':
    app.run(debug=True)

