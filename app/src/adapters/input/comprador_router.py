# app/adapters/input/fastapi_controller.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.domain.comprador import Comprador
from src.application.usecase.cadastrar_comprador_usecase import CadastrarCompradorUseCase
from src.adapters.output.repository.repository import Repository
from src.adapters.output.repository.comprador_repository import CompradorRepository

repository : Repository = CompradorRepository()
use_case = CadastrarCompradorUseCase(repository)
router = APIRouter()

class CompradorInput(BaseModel):
    nome: str
    cpf: str
    email: str
    endereco: str


@router.post(path="/", status_code=status.HTTP_201_CREATED)
def cadastrar(input: CompradorInput):
    comprador :Comprador = use_case.executar(input.nome, input.cpf, input.email, input.endereco)
    return comprador

@router.get(path="/{comprador_id}",status_code=status.HTTP_200_OK)
def buscar(comprador_id: str):
    comprador :Comprador = repository.findById(comprador_id)
    return comprador.normalize(comprador)
