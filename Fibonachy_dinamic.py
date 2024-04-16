def fibonacci_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
    return memo[n]

# Пример использования
print(fibonacci_dynamic(10))  # Выводит 55
