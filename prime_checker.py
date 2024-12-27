def prime_checker(number):
    is_prime = True

    for num in range(2, number // 2 + 1):
        if number % num == 0:
            is_prime = False
            break

    return is_prime

n = int(input("Select a number: "))
print(prime_checker(number=n))