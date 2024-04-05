from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manual-character-creation')
def manual_character_creation():
    return render_template('character_creation.html')

@app.route('/smart-character-creation')
def smart_character_creation():
    # Your logic here
    return render_template('smart_character_creation.html')

@app.route('/books')
def books():
    # Your logic here
    return render_template('books.html')


if __name__ == '__main__':
    app.run(debug=True)

