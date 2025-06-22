from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Halo, Flask berhasil dijalankan!'

@app.route('/hello/<name>')
def hello(name):
    return f'Halo, {name}! Selamat datang di aplikasi Flask.'

if __name__ == '__main__':
    app.run(debug=True)
