import pytest

from hgt.tarea import Tarea
@pytest.fixture
def tarea():
    return Tarea(False,1,"Dibujar un pato")

def test_read(tarea):
    assert tarea.read() == (False,1,"Dibujar un pato")

def test_update(tarea):
    tarea.update(True,2,"Matar a Dios")

    assert tarea.read() == (True,2,"Matar a Dios")


def test_delete(tarea):
    tarea.delete()

    assert tarea.read() == (None,None,None)