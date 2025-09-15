from src.domain.comprador import Comprador
from src.adapters.output.repository.repository import Repository

class CadastrarCompradorUseCase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def executar(self, nome, cpf, email, endereco):
        comprador = Comprador.criar(nome, cpf, email, endereco)
        self.repository.save(comprador)
        return comprador
