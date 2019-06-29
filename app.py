from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')
@app.route('/author')
def about_author():
    return 'This webpage have been created by Michal Madera'

if __name__ == "__main__":
    app.run()
