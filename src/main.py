def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print("=== CALCULADORA SIMPLES ===")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Soma:", soma(num1, num2))
    print("Subtração:", subtracao(num1, num2))
    print("Multiplicação:", multiplicacao(num1, num2))

    resultado_div = divisao(num1, num2)
    if resultado_div is not None:
        print("Divisão:", resultado_div)
    else:
        print("Não é possível dividir por zero")

    print("Obrigado por usar a calculadora!!!!!!")