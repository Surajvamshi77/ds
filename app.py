from flask import Flask
app = Flask(__name__)
@app.route('/')
def homepage():
    return "WELCOME"
@app.route('/search')
def search_page():
    return "HELLO"
if __name__ == '__main__':
    app.run()