from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Welcome to the main page'

def about_author('/author'):
    return 'This webpage have been created by Michal Madera'

if __name__ == "__main__":
    app.run()
