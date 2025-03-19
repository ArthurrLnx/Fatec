from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)
app.app_context().push()
mydb = mysql.connector.connect(
	host="localhost",
	port="3306",
	user="root",
	password="",
	database="produtosbd"
	)

mycursor = mydb.cursor(buffered=True)


@app.route('/')
def principal():
		return render_template("index_mysql.html")


@app.route('/categorias', methods=["POST", "GET"])
def categorias_func():
	if request.method == "POST":
		if request.form.get("id") and request.form.get("nome"):
			id_var=request.form.get("id")
			nome_var=request.form.get("nome")
			sql = "INSERT INTO categoria (ID, NOME) VALUES (%s, %s)"
			val = (id_var, nome_var)
			mycursor.execute(sql, val)
			mydb.commit()

			if mycursor.rowcount>=1:
				return redirect(url_for('listar_func'))
			else:
				print("erro")
				return redirect(url_for('listar_func'))
				
	return render_template("categorias.html")

@app.route('/sucesso')
def sucesso_func():

	return render_template("sucesso.html")

@app.route('/listar')
def listar_func():

	mycursor.execute("SELECT * FROM categoria")
	myresult = mycursor.fetchall()
	
	return render_template("lista_categorias.html", categorias=myresult)

@app.route('/<int:id>/remove_categoria')
def remove_categoria(id):
	sql = "DELETE from categoria where id=%s"
	val = (id,)
	mycursor.execute(sql, val)
	mydb.commit()
	return redirect(url_for('listar_func'))

@app.route('/<int:id>/editar_categoria', methods=["GET","POST"])
def editar_categoria(id):

	sql="SELECT * FROM categoria where id=%s"
	val = (id,)
	mycursor.execute(sql, val)
	myresult = mycursor.fetchone()

	if request.method == "POST":
		if request.form.get("id") and request.form.get("nome"):
			id_var=request.form.get("id")
			nome_var=request.form.get("nome")
			sql = "UPDATE categoria set nome=%s where id=%s"
			val = (nome_var, id_var)
			mycursor.execute(sql, val)
			mydb.commit()

			if mycursor.rowcount>=1:
				return redirect(url_for('listar_func'))
			else:
				print("erro")
				return redirect(url_for('listar_func'))
				
	return render_template("editar_categoria.html", id=myresult[0], nome=myresult[1])


if __name__ == "_main__":

	app.run(debug=True)