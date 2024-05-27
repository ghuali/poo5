import pytest
from examenRepaso.perusoma import Persona


@pytest.fixture
def persona():
    return Persona('William')

def test_create(persona):
    assert persona.read() == 'William'