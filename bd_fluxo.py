
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="fluxo"
    )




mycursor = banco.cursor()


#mycursor.execute("DROP DATABASE fluxo")

#mycursor.execute("CREATE DATABASE fluxo")
'''

mycursor.execute("CREATE TABLE registrar_carro(id_veiculo SMALLINT AUTO_INCREMENT , marca_veiculo VARCHAR(50), placa_veiculo VARCHAR(15), modelo_veiculo VARCHAR(20), ano_veiculo SMALLINT, CONSTRAINT idveiculopk PRIMARY KEY (id_veiculo))")


mycursor.execute("CREATE TABLE registrar_motorista(id_motorista SMALLINT AUTO_INCREMENT , nome_motorista VARCHAR(100), cnh BIGINT, endereco VARCHAR(100), cidade VARCHAR(60), estado VARCHAR(60), cep BIGINT, celular BIGINT, email VARCHAR(100), CONSTRAINT idmotoristapk PRIMARY KEY (id_motorista))")


mycursor.execute("CREATE TABLE registrar_viagem(id_viagem SMALLINT AUTO_INCREMENT , data_viagem DATE, nome_motorista SMALLINT, local VARCHAR(25), valor_viagem BIGINT, valor_combustivel BIGINT, valor_pedagio BIGINT, nome_empresa VARCHAR(60), placa_veiculo SMALLINT, observacao VARCHAR(150), CONSTRAINT idviagempk PRIMARY KEY (id_viagem), CONSTRAINT fkmotorista FOREIGN KEY (nome_motorista) REFERENCES registrar_motorista(id_motorista), CONSTRAINT fkplaca FOREIGN KEY (placa_veiculo) REFERENCES registrar_carro(id_veiculo))")



mycursor.execute("CREATE TABLE tipo_Pessoa(id_tipo_pessoa CHAR(1) NOT NULL , descricao VARCHAR(16),constraint pkTipoPessoa primary key (id_tipo_pessoa))")

mycursor.execute("INSERT INTO tipo_Pessoa(id_tipo_pessoa, descricao) values ('1', 'administrador')")
mycursor.execute("INSERT INTO tipo_Pessoa(id_tipo_pessoa, descricao) values ('2', 'usuario')")
'''

mycursor.execute("CREATE TABLE usuario(id_usuario SMALLINT  AUTO_INCREMENT NOT NULL , nome_usuario VARCHAR(40), email_usuario VARCHAR(40), dt_cadastro DATE, senha_aplicacao VARCHAR(500), id_tipo_pessoa CHAR(1), CONSTRAINT pkcod_usuario PRIMARY KEY (id_usuario), CONSTRAINT uq_email_usuario  UNIQUE (email_usuario), CONSTRAINT fktipopessoa FOREIGN KEY (id_tipo_pessoa) REFERENCES tipo_pessoa(id_tipo_pessoa))")

mycursor.execute("INSERT INTO usuario(nome_usuario,email_usuario,senha_aplicacao, id_tipo_pessoa) VALUES ('ADMINISTRADOR','administrador@administrador.com','91f5167c34c400758115c2a6826ec2e3', '1')")

banco.commit()
banco.close()