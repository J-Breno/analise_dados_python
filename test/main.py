def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro

def calcular_faturamento():
    vendas = [1000, 2000, 3000, 4000, 5000]
    faturamento = sum(vendas)
    return faturamento

print(calcular_lucro(120, 200))
