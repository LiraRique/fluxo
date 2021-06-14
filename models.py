class form_carro:
    def __init__(self,marca_veiculo, placa_veiculo, modelo_veiculo, ano_veiculo, id_veiculo=None):
        self.marca_veiculo = marca_veiculo
        self.placa_veiculo = placa_veiculo
        self.modelo_veiculo = modelo_veiculo
        self.ano_veiculo = ano_veiculo
        self.id_veiculo = id_veiculo


class form_motorista:
    def __init__(self,nome_motorista, cnh, endereco, cidade, estado, cep, celular, email, id_motorista=None):
        self.nome_motorista = nome_motorista
        self.cnh = cnh
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.celular = celular
        self.email = email
        self.id_motorista = id_motorista

class form_viagem:
    def __init__(self, data_viagem, nome_motorista , local, valor_viagem, valor_combustivel, valor_pedagio, nome_empresa, placa_veiculo, observacao, id_viagem=None):
        self.data_viagem = data_viagem
        self.nome_motorista  = nome_motorista 
        self.local = local
        self.valor_viagem = valor_viagem
        self.valor_combustivel = valor_combustivel
        self.valor_pedagio = valor_pedagio
        self.nome_empresa = nome_empresa
        self.placa_veiculo = placa_veiculo
        self.observacao = observacao
        self.id_viagem = id_viagem


class exibe_motorista:
    def __init__(self, id_motorista, nome_motorista):
        self.id_motorista = id_motorista
        self.nome_motorista = nome_motorista

class exibe_placa:
    def __init__(self, id_veiculo, placa_veiculo):
        self.id_veiculo = id_veiculo
        self.placa_veiculo = placa_veiculo

class exibe_viagem:
    def __init__(self, data_viagem, local, valor_viagem, valor_combustivel, valor_pedagio, observacao):
        self.data_viagem = data_viagem
        self.local = local
        self.valor_viagem = valor_viagem
        self.valor_combustivel = valor_combustivel
        self.valor_pedagio = valor_pedagio
        self.observacao = observacao

