import unittest
from unittest.mock import MagicMock, patch
from src.application.usecase.cadastrar_comprador_usecase import CadastrarCompradorUseCase
from src.domain.comprador import Comprador

class TestCadastrarCompradorUseCase(unittest.TestCase):

    @patch("src.domain.comprador.Comprador.criar")
    def test_executar_deve_criar_e_salvar_comprador(self, mock_criar):
        # Arrange
        mock_repository = MagicMock()
        usecase = CadastrarCompradorUseCase(repository=mock_repository)

        nome = "João Silva"
        cpf = "12345678900"
        email = "joao@email.com"
        endereco = "Rua A, 123"

        comprador_mock = MagicMock(spec=Comprador)
        mock_criar.return_value = comprador_mock

        resultado = usecase.executar(nome, cpf, email, endereco)

        mock_criar.assert_called_once_with(nome, cpf, email, endereco)
        mock_repository.save.assert_called_once_with(comprador_mock)
        self.assertEqual(resultado, comprador_mock)

if __name__ == "__main__":
    unittest.main()
