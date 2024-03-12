def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = int(input("Digite um Número: "))
if num in fibonacci(num * 10):
    index = 1 + fibonacci(num * 10).index(num)
    print(f"{num} é o {index} número na sequência de Fibonacci 0 e 1.")
else:
    print(f"{num} não está na sequência de Fibonacci de 0 e 1.")