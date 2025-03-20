from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection
from models import Pessoa, Animal, Medico, Funcionario, Cliente, Agendamento

app = Flask(__name__)
app.app_context().push()
mydb = mysql.connector.connect(
	host="localhost",
	port="3306",
	user="root",
	password="",
	database="vetbd"
	)

mycursor = mydb.cursor(buffered=True)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/cadastrar_pessoa', methods=["POST", "GET"])
def cadastrar_pessoa():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        endereco = request.form.get("endereco")
        cpf = request.form.get("cpf")

        pessoa = Pessoa(nome, telefone, email, endereco, cpf)
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        sql = "INSERT INTO pessoa (nome, telefone, email, endereco, cpf) VALUES (%s, %s, %s, %s, %s)"
        val = (pessoa.nome, pessoa.telefone, pessoa.email, pessoa.endereco, pessoa.cpf)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('principal'))

    return render_template("cadastrar_pessoa.html")

@app.route('/cadastrar_animal', methods=["POST", "GET"])
def cadastrar_animal():
    if request.method == "POST":
        nome = request.form.get("nome")
        sexo = request.form.get("sexo")
        peso = request.form.get("peso")
        especie = request.form.get("especie")
        raca = request.form.get("raca")
        data_nascimento = request.form.get("data_nascimento")

        animal = Animal(nome, sexo, peso, especie, raca, data_nascimento)
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        sql = "INSERT INTO animal (nome, sexo, peso, especie, raca, data_nascimento) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (animal.nome, animal.sexo, animal.peso, animal.especie, animal.raca, animal.data_nascimento)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('principal'))

    return render_template("cadastrar_animal.html")

@app.route('/agendar_consulta', methods=["POST", "GET"])
def agendar_consulta():
    if request.method == "POST":
        data = request.form.get("data")
        medico_id = request.form.get("medico")
        cliente_id = request.form.get("cliente")
        funcionario_id = request.form.get("funcionario")
        valor = request.form.get("valor")

        mydb = get_db_connection()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM pessoa WHERE id = %s", (medico_id,))
        medico = mycursor.fetchone()
        mycursor.execute("SELECT * FROM pessoa WHERE id = %s", (cliente_id,))
        cliente = mycursor.fetchone()
        mycursor.execute("SELECT * FROM pessoa WHERE id = %s", (funcionario_id,))
        funcionario = mycursor.fetchone()

        agendamento = Agendamento(data, medico, cliente, funcionario, valor=valor)
        sql = "INSERT INTO agendamento (data, medico_id, cliente_id, funcionario_id, valor) VALUES (%s, %s, %s, %s, %s)"
        val = (agendamento.data, medico_id, cliente_id, funcionario_id, agendamento.valor)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('listar_consultas'))

    return render_template("agendar_consulta.html")

@app.route('/listar_consultas')
def listar_consultas():
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM agendamento")
    consultas = mycursor.fetchall()
    return render_template("listar_consultas.html", consultas=consultas)

if __name__ == "__main__":
    app.run(debug=True)