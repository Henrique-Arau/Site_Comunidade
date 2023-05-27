from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Beleza, Meu 1º site está no ar!!!!!!!!!!! To sabendo muito'


@app.route('/contato')
def contato():
    return 'Qualquer dúvida mande um e-mail pata listavip@hashtagtreinamentos.com'


if __name__ == '__main__':
    app.run(debug=True)



