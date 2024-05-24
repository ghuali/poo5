import pytest
from hgt.evento import Evento
from hgt.tarea import Tarea

@pytest.fixture
def evento():
    
    return Evento(Tarea.True,Tarea.4,Tarea."matar a satanas","30-5-2024","31-5-2024","12:30","23:59")

def test_read(evento):
    assert evento.read() == (True,4,"matar a satanas","30-5-2024","31-5-2024","12:30","23:59")

def test_update(evento):
    evento.update(True,2,"Matar a Dios")

    assert evento.read() == (True,2,"Matar a Dios")


def test_delete(evento):
    evento.delete()

    assert evento.read() == (None,None,None)