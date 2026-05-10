def factorial(n):
    if n == 0 or n == 1:
        return 1
    # Hasil üçün 1-dən başlayırıq
    result = 1
    # n-in özünü də hesablamaq üçün n + 1 yazırıq
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))