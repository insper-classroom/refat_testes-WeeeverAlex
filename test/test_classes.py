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
def test_endereco_sem_num():
    with pytest.raises(TypeError) as exc:
        assert exc == Endereco(cep=f'045460420')

@pytest.mark.endereco
def test_consulta_cep_nao_e_string_ou_int():
    with pytest.raises(TypeError) as exc:
        Endereco.consultar_cep(cep=False)
        assert 'missing' in str(exc.value)

@pytest.mark.endereco
def test_cep_formato_numerico_errado():
    with pytest.raises(TypeError) as exc:
        Endereco.consultar_cep(cep=99999)
        assert 'length' in str(exc.value)

@pytest.mark.endereco
def test_caiu_a_net():
    pass

#PESSOA_FISICA
#@pytest.mark.pessoa_fisica

#CARRINHO
 #@pytest.mark.carrinho

#PEDIDO
#@pytest.mark.pedido
