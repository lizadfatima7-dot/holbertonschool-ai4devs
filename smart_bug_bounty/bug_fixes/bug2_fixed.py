def factorial(n):
    if n == 0 or n == 1:
        return 1
    # Hasilin 0 olmaması üçün result=1 edildi və n daxil olmaqla range quruldu
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result