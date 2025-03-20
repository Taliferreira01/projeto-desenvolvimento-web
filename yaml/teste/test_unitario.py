def soma(a, b):
    return a + b

resultado = soma(5, 3)

print(resultado)


def test_minha_funcao():
    resultado = soma(a = 1 , b = 2)

    assert resultado == 3
