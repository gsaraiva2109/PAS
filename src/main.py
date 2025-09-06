from datetime import date
from enum import Enum
from typing import List, Optional


class TipoArea(Enum):
    CHURRASQUEIRA = "Churrasqueira"
    SALAO_DE_FESTAS = "Salão de Festas"
    QUADRA = "Quadra"

class TipoVeiculo(Enum):
    CARRO = "Carro"
    MOTO = "Moto"

class Setor:
    def __init__(self, nome: str):
        self.nome = nome

class Funcao:
    def __init__(self, nome: str):
        self.nome = nome

class Pessoa:
    def __init__(self, nome: str, cpf: str, data_nascimento: date):
        self.nome: str = nome
        self.cpf: str = cpf
        self.data_nascimento: date = data_nascimento

    def _entrar(self):
        print(f"{self.nome} entrou.")

    def _sair(self):
        print(f"{self.nome} saiu.")


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, setor: Setor, funcao: Funcao):
        super().__init__(nome, cpf, data_nascimento)
        self.setor: Setor = setor
        self.funcao: Funcao = funcao


class Area:
    def __init__(self, tamanho: float, tipo_area: TipoArea):
        self.tamanho: float = tamanho
        self.tipo_area: TipoArea = tipo_area


class Veiculo:
    def __init__(self, placa: str, modelo: str, cor: str, tipo_veiculo: TipoVeiculo):
        self.placa: str = placa
        self.modelo: str = modelo
        self.cor: str = cor
        self.tipo_veiculo: TipoVeiculo = tipo_veiculo


class Morador(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, bloco: int, numero: int):
        super().__init__(nome, cpf, data_nascimento)
        self.bloco: int = bloco
        self.numero: int = numero
        self.veiculo: Optional[Veiculo] = None

    def reservar_area(self, area: Area) -> None:
        print(f"O morador {self.nome} reservou a área: {area.tipo_area.value}.")


class Visitante(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, morador_anexado: Morador):
        super().__init__(nome, cpf, data_nascimento)
        self.morador_anexado: Morador = morador_anexado


class MoradorVisitante:
    def __init__(self, morador: Morador, visitante: Visitante, periodo_estadia: date):
        self.morador: Morador = morador
        self.visitante: Visitante = visitante
        self.periodo_estadia: date = periodo_estadia