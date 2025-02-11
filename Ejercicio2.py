# Crea un programa el cual imprima una lista con los primeros 15 números de la sucesión de Fibonacci.
def fibonacci(n):
    fibo = [0, 1]
    for _ in range(n - 2):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

print("Sucesión de Fibonacci:", fibonacci(15))
