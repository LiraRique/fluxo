#################################### APLICAÇÃO FLASK #####################################
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from models import form_carro, form_motorista, form_viagem
from metodos import metodo_cadastrar, exibe_nomes
from datetime import timedelta
import MySQLdb



app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

banco = MySQLdb.connect(user='ijmdmqnlisth7wws', passwd='tmveztghuiukqm2n', host='qao3ibsa7hhgecbv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', database='da4l2sdpuhx3zt6c')

db = banco.cursor()

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

cadastros_forms= metodo_cadastrar.cadastros(db)
exibe_motoristas= exibe_nomes.exibe(db)

####################################        VIEWS ADMINISTRADOR       ######################

@app.route('/')
def pagina_fluxo():
    return render_template('pagina_fluxo.html')


@app.route('/registrar_carro')
def registrar_carro():
    return render_template('registrar_carro.html')


@app.route('/registrar_motorista')
def registrar_motorista():
    return render_template('registrar_motorista.html')


@app.route('/registrar_viagem')
def registrar_viagem():
    lista_moto= exibe_motoristas.exibe_motorista_bd()
    list_placa= exibe_motoristas.exibe_placa_bd()
    return render_template('registrar_viagem.html',lista_motorista = lista_moto, lista_placa = list_placa)



@app.route('/consultar_janeiro')
def consultar_janeiro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_janeiro()  
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('01')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('01')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = 'Janeiro'
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_fevereiro')
def consultar_fevereiro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_fevereiro()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('02')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('02')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = 'Fevereiro'
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_marco')
def consultar_marco():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_marco()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('03')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('03')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = 'Março'
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )

@app.route('/consultar_abril')
def consultar_abril():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_abril()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('04')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('04')
    valor_liquido = "R$ {%.2f}".format(soma_valor_bruto - somacombustivel_pedagio)
    data = "Abril"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )

@app.route('/consultar_maio')
def consultar_maio():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_maio()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('05')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('05')
    combustivel_pedagio =  '{:.2f}'.format(somacombustivel_pedagio)
    valor_bruto =  '{:.2f}'.format(soma_valor_bruto)
    valor_liquido = '{:.2f}'.format(soma_valor_bruto - somacombustivel_pedagio)
    data = 'Maio'
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = combustivel_pedagio, svalorbruto = valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_junho')
def consultar_junho():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_junho()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('06')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('06')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Junho"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_julho')
def consultar_julho():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_julho()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('07')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('07')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Julho"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_agosto')
def consultar_agosto():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_agosto()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('08')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('08')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Agosto"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )


@app.route('/consultar_setembro')
def consultar_setembro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_setembro()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('09')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('09')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Setembro"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )

@app.route('/consultar_outubro')
def consultar_outubro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_outubro()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('10')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('10')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Outubro"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )

@app.route('/consultar_novembro')
def consultar_novembro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_novembro()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('11')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('11')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = 'Novembro'
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )

@app.route('/consultar_dezembro')
def consultar_dezembro():
    lista_viagem_bd = exibe_motoristas.exibe_viagem_dezembro()
    somacombustivel_pedagio = exibe_motoristas.soma_combustivel_pedagio('12')
    soma_valor_bruto = exibe_motoristas.soma_valor_bruto('12')
    valor_liquido = soma_valor_bruto - somacombustivel_pedagio
    data = "Dezembro"
   
    return render_template('consultar_mes.html', lista_viagem = lista_viagem_bd, soma_gastos = somacombustivel_pedagio, svalorbruto = soma_valor_bruto, vliquido = valor_liquido, dviagem = data )






@app.route('/cadastrar_carro', methods= ['POST',])
def cadastrar_carro():
    marca_veiculo = request.form['marca']
    placa_veiculo = request.form['placa']
    modelo_veiculo = request.form['modelo']
    ano_veiculo = request.form['ano_veiculo']
  
    cadastro_models= form_carro(marca_veiculo, placa_veiculo, modelo_veiculo, ano_veiculo)
    cadastro_bd = cadastros_forms.cadastrar_carro_sistema(cadastro_models)
    flash('Veiculo cadastrado com sucesso!')
    return redirect(url_for('pagina_fluxo'))




@app.route('/cadastrar_motorista', methods= ['POST',])
def cadastrar_motorista():
    nome_motorista = request.form['nome_motorista']
    cnh = request.form['cnh']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cep = request.form['cep']
    celular = request.form['celular']
    email = request.form['email']
  
    cadastro_models= form_motorista(nome_motorista, cnh, endereco, cidade, estado, cep, celular,email)
    cadastro_bd = cadastros_forms.cadastrar_motorista_sistema(cadastro_models)

    flash('Motorista cadastrado com sucesso!')
    return redirect(url_for('pagina_fluxo'))




@app.route('/cadastrar_viagem', methods= ['POST',])
def cadastrar_viagem():
    data_viagem = request.form['data_viagem']
    nome_motorista = request.form['nome_motorista']
    local_viagem = request.form['local_viagem']
    valor_viagem = request.form['valor_viagem']
    valor_combustivel = request.form['valor_combustivel']
    valor_pedagio = request.form['valor_pedagio']
    nome_empresa = request.form['nome_empresa']
    placa_veiculo = request.form['placa_veiculo']
    observacao = request.form['observacao']
  
    cadastro_models= form_viagem(data_viagem, nome_motorista, local_viagem, valor_viagem, valor_combustivel, valor_pedagio, nome_empresa, placa_veiculo, observacao)
    cadastro_bd = cadastros_forms.cadastrar_viagem_sistema(cadastro_models)

    flash('Viagem cadastrada com sucesso!')
    return redirect(url_for('pagina_fluxo'))



if __name__=='__main__':
    app.run(debug=True)
