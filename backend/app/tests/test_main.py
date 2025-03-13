from app.services import classify_client

def test_classification():
    assert classify_client(9000, 1000) == "Azul"
    assert classify_client(5000, 1000) == "Verde"
    assert classify_client(2500, 1000) == "Amarillo"
    assert classify_client(1200, 500) == "Rojo"
