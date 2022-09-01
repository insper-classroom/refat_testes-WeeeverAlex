import pytest
import numpy as np
from classes.Endereco import Endereco

#ENDEREÇO
@pytest.mark.endereco
def test_endereco_sem_cep():
    with pytest.raises(TypeError) as exc:
        assert exc == Endereco(numero=123)

@pytest.mark.endereco
def test_cep_nao_existente():
    assert '' == Endereco.consultar_cep(cep=99999999) 

@pytest.mark.endereco
def test_cep_existente():     

#PESSOA_FISICA
#@pytest.mark.pessoa_fisica

#CARRINHO
 #@pytest.mark.carrinho

#PEDIDO
#@pytest.mark.pedido
