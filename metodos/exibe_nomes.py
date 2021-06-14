from models import exibe_motorista,exibe_placa, exibe_viagem


SQL_BUSCAR_MOTORISTA = '''select id_motorista, nome_motorista from registrar_motorista'''

SQL_BUSCAR_PLACA = 'select id_veiculo, placa_veiculo from registrar_carro'


SQL_JANEIRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "01"'
SQL_FEVEREIRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "02"'
SQL_MARCO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "03"'
SQL_ABRIL ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "04"'
SQL_MAIO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "05"'
SQL_JUNHO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "06"'
SQL_JULHO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "07"'
SQL_AGOSTO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "08"'
SQL_SETEMBRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "09"'
SQL_OUTUBRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "10"'
SQL_NOVEMBRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "11"'
SQL_DEZEMBRO ='select DATE_FORMAT(data_viagem, "%d/%m/%y"), local, valor_viagem, valor_combustivel, valor_pedagio, observacao from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%m") = "12"'

select_combustivel = '''select valor_combustivel from registrar_viagem WHERE  DATE_FORMAT(data_viagem, "%%m") = %s'''

select_pedagio = '''select valor_pedagio from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%%m") = %s'''

select_valor_bruto = '''select valor_viagem from registrar_viagem WHERE DATE_FORMAT(data_viagem, "%%m") = %s'''


class exibe:
    def __init__(self, db):
        self.__db = db


    def exibe_motorista_bd(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCAR_MOTORISTA)
        motorista = traduz_nome(cursor.fetchall())
        return motorista

    def exibe_placa_bd(self):
        cursor = self.__db
        cursor.execute(SQL_BUSCAR_PLACA)
        placa_veiculo = traduz_placa(cursor.fetchall())
        return placa_veiculo
    
    
    def exibe_viagem_janeiro(self):
        cursor = self.__db
        cursor.execute(SQL_JANEIRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    def exibe_viagem_fevereiro(self):
        cursor = self.__db
        cursor.execute(SQL_FEVEREIRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_marco(self):
        cursor = self.__db
        cursor.execute(SQL_MARCO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_abril(self):
        cursor = self.__db
        cursor.execute(SQL_ABRIL)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_maio(self):
        cursor = self.__db
        cursor.execute(SQL_MAIO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    def exibe_viagem_junho(self):
        cursor = self.__db
        cursor.execute(SQL_JUNHO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_julho(self):
        cursor = self.__db
        cursor.execute(SQL_JULHO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    def exibe_viagem_agosto(self):
        cursor = self.__db
        cursor.execute(SQL_AGOSTO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_setembro(self):
        cursor = self.__db
        cursor.execute(SQL_SETEMBRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_outubro(self):
        cursor = self.__db
        cursor.execute(SQL_OUTUBRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_novembro(self):
        cursor = self.__db
        cursor.execute(SQL_NOVEMBRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo
    
    
    
    def exibe_viagem_dezembro(self):
        cursor = self.__db
        cursor.execute(SQL_DEZEMBRO)
        viagem_veiculo = traduz_viagem(cursor.fetchall())
        return viagem_veiculo

    def soma_combustivel_pedagio(self, id):
         cursor = self.__db.connection.cursor()
         cursor.execute(select_combustivel,(id,))
         lista = []
         for x in cursor.fetchall():
             lista.append(x[0])
         combustivel = 0
         for y in lista:
             combustivel += y
         cursor.execute(select_pedagio,(id,))
         lista_pedagio =[]
         for x in cursor.fetchall():
              lista_pedagio.append(x[0])
         pedagio = 0
         for y in lista_pedagio:
             pedagio += y
         soma = combustivel + pedagio
         return soma

    def soma_valor_bruto(self, id):
        cursor = self.__db
        cursor.execute(select_valor_bruto,(id,))
        lista = []
        for x in cursor.fetchall():
            lista.append(x[0])
        valor_bruto = 0
        for y in lista:
            valor_bruto += y
        print(valor_bruto)
        return valor_bruto


def traduz_nome(lista_motorista):
    def cria_usuario_com_tupla(tupla):
        
        
        return exibe_motorista(tupla[0], tupla[1])
        
    return list(map(cria_usuario_com_tupla, lista_motorista))



def traduz_placa(lista_placa):
    def cria_placa_com_tupla(tupla):
        
        
        return exibe_placa(tupla[0], tupla[1])
        
    return list(map(cria_placa_com_tupla, lista_placa))



def traduz_viagem(lista_viagem):
    def cria_viagem_com_tupla(tupla):
        
        
        return exibe_viagem(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
        
    return list(map(cria_viagem_com_tupla, lista_viagem))



