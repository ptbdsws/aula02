from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route("/")
def home():
    return
    """
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="{url_for('home')}">Home</a></li>
        <li><a href="{url_for('identification', name='Gustavo de Oliveira Martins', pt='PT3031772', institution='IFSP')}">Identificação</a></li>
        <li><a href="{url_for('contextrequest')}">Contexto da requisição</a></li>
    </ul>
    """

@app.route("/user/<name>/<pt>/<institution>")
def identification(name, pt, institution):
    return
    """
    <h1>Avaliação contínua: Aula 030</h1>

    <h2><b>Aluno:</b> {name}</h2>
    <h2><b>Prontuário:</b> {pt}</h2>
    <h2><b>Instituição:</b> {institution}</h2>

    <p><a href="{url_for('home')}">Voltar</a></p>
    """

@app.route("/contextorequisicao")
def contextrequest():
    user_agent = request.headers.get("User-Agent", "desconhecido")
    remote_ip = request.remote_addr or "desconhecido"
    host = request.host

    return 
    """
    <h1>Avaliação contínua: Aula 030</h1>

    <h2><b>Seu navegador é: {user_agent}</b></h2>
    <h2><b>O IP do computador remoto é: {remote_ip}</b></h2>
    <h2><b>O host da aplicação é: {host}</b></h2>

    <p><a href="{url_for('home')}">Voltar</a></p>
    """
