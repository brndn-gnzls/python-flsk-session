from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask Setup"

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))