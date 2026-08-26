from main import calcular_lucro, calcular_faturamento

def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento, 200) > 0

def test_calcular_faturamento():
    assert type(calcular_faturamento()) == int

# asset é para verificar, ele vai retornar verdadeiro ou falso