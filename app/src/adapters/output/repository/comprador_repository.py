from src.adapters.output.repository.repository_default import RepositoryDefault
from src.domain.comprador import Comprador

class CompradorRepository(RepositoryDefault[Comprador, str]):
    def __init__(self) -> None:
        super().__init__(Comprador)


    def parseToModel(self, dict):
        return Comprador.parseToModel(dict)
