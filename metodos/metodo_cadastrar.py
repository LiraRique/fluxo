from models import form_carro, form_motorista, form_viagem, usuario


SQL_CADASTRAR_VEICULO = 'INSERT INTO registrar_carro(marca_veiculo, placa_veiculo, modelo_veiculo, ano_veiculo) VALUES (%s, %s, %s, %s)'

SQL_CADASTRAR_MOTORISTA = 'INSERT INTO registrar_motorista(nome_motorista, cnh, endereco, cidade, estado, cep, celular, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

SQL_CADASTRAR_VIAGEM = 'INSERT INTO registrar_viagem(data_viagem, nome_motorista , local, valor_viagem, valor_combustivel, valor_pedagio, nome_empresa, placa_veiculo, observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

SQL_CADASTRAR_LOGIN_MOTORISTA = 'INSERT INTO usuario(nome_usuario, email_usuario, dt_cadastro, senha_aplicacao, id_tipo_pessoa) values (%s, %s, %s, %s, %s)'

class cadastros:
    def __init__(self, db):
        self.__db = db


    def cadastrar_carro_sistema(self, form_carro):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CADASTRAR_VEICULO, (form_carro.marca_veiculo, form_carro.placa_veiculo, form_carro.modelo_veiculo, form_carro.ano_veiculo))
        self.__db.connection.commit()
    
    def cadastrar_motorista_sistema(self, form_motorista):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CADASTRAR_MOTORISTA, (form_motorista.nome_motorista, form_motorista.cnh, form_motorista.endereco, form_motorista.cidade, form_motorista.estado, form_motorista.cep, form_motorista.celular, form_motorista.email))
        self.__db.connection.commit()
    
    def cadastrar_viagem_sistema(self, form_viagem):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CADASTRAR_VIAGEM, (form_viagem.data_viagem, form_viagem.nome_motorista, form_viagem.local, form_viagem.valor_viagem, form_viagem.valor_combustivel, form_viagem.valor_pedagio, form_viagem.nome_empresa, form_viagem.placa_veiculo, form_viagem.observacao))
        self.__db.connection.commit()
    
    def cadastrar_login_motorista(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CADASTRAR_LOGIN_MOTORISTA, (usuario.nome_usuario, usuario.email_usuario, usuario.dt_cadastro, usuario.senha_aplicacao, usuario.id_tipo_pessoa))
        self.__db.connection.commit()
    

