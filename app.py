from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return index.html
@app.route('/author')
def about_author():
    return 'This webpage have been created by Michal Madera'

if __name__ == "__main__":
    app.run()
