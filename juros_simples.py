def decorator_imprimir(func):
    def wrapper(capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}')
        print(f'RESULTADO: {resultado}')
        return resultado
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    juros = capital * (taxa/100) * tempo
    return juros

juros_simples(1000, 5, 6)
