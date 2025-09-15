# app/domain/comprador.py

import uuid
from dataclasses import dataclass
from src.util.crypto import criptografar, descriptografar


@dataclass
class Comprador:
    _id: str
    nome: str
    cpf: str
    email: str
    endereco: str

    @staticmethod
    def criar(nome: str, cpf: str, email: str, endereco: str) -> 'Comprador':
        return Comprador(
            _id=str(uuid.uuid4()),
            nome=criptografar(nome),
            cpf=criptografar(cpf),
            email=criptografar(email),
            endereco=criptografar(endereco),
        )


    @classmethod
    def normalize(cls, dataLGPD):
        compradorNormalize = cls(
            _id=dataLGPD._id,
            nome=descriptografar(dataLGPD.nome),
            cpf=descriptografar(dataLGPD.cpf),
            email=descriptografar(dataLGPD.email),
            endereco=descriptografar(dataLGPD.endereco)
        )    
        compradorNormalize._id = dataLGPD._id
        return compradorNormalize

    @classmethod
    def parseToModel(cls, dataDict):
        return cls(**dataDict)
    

