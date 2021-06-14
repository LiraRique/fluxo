
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


mycursor.execute("CREATE TABLE registrar_carro(id_veiculo SMALLINT AUTO_INCREMENT , marca_veiculo VARCHAR(50), placa_veiculo VARCHAR(15), modelo_veiculo VARCHAR(20), ano_veiculo SMALLINT, CONSTRAINT idveiculopk PRIMARY KEY (id_veiculo))")


mycursor.execute("CREATE TABLE registrar_motorista(id_motorista SMALLINT AUTO_INCREMENT , nome_motorista VARCHAR(100), cnh BIGINT, endereco VARCHAR(100), cidade VARCHAR(60), estado VARCHAR(60), cep BIGINT, celular BIGINT, email VARCHAR(100), CONSTRAINT idmotoristapk PRIMARY KEY (id_motorista))")


mycursor.execute("CREATE TABLE registrar_viagem(id_viagem SMALLINT AUTO_INCREMENT , data_viagem DATE, nome_motorista SMALLINT, local VARCHAR(25), valor_viagem BIGINT, valor_combustivel BIGINT, valor_pedagio BIGINT, nome_empresa VARCHAR(60), placa_veiculo SMALLINT, observacao VARCHAR(150), CONSTRAINT idviagempk PRIMARY KEY (id_viagem), CONSTRAINT fkmotorista FOREIGN KEY (nome_motorista) REFERENCES registrar_motorista(id_motorista), CONSTRAINT fkplaca FOREIGN KEY (placa_veiculo) REFERENCES registrar_carro(id_veiculo))")
