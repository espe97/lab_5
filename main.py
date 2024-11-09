import random

def fermat_primality_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False  
    return True  
def jacobi_symbol(a, n):
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a  
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

def solovay_strassen_test(n, k=5):
    
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = jacobi_symbol(a, n)
        if x == 0 or pow(a, (n - 1) // 2, n) != (x % n):
            return False  
    return True  

def miller_rabin_primality_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  
    return True 

n = int(input("Введите число для проверки на простоту: "))
k = int(input("Введите количество итераций для повышения надёжности: "))

# Вывод результатов
print("\nРезультаты проверки числа", n, "на простоту:")
print("Тест Ферма:", "Вероятно простое" if fermat_primality_test(n, k) else "Составное")

# Символ Якоби вычисляется для примера с a = 2, можно изменить на другое значение
a_for_jacobi = int(input("\nВведите значение a для вычисления символа Якоби (a/n): "))
print(f"Символ Якоби для a={a_for_jacobi} и n={n}:", jacobi_symbol(a_for_jacobi, n))

print("Тест Соловея-Штрассена:", "Вероятно простое" if solovay_strassen_test(n, k) else "Составное")
print("Тест Миллера-Рабина:", "Вероятно простое" if miller_rabin_primality_test(n, k) else "Составное")
