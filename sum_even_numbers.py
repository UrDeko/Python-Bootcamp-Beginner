def sum_even_numbers(low, high):
    result = 0
    low = low if low % 2 == 0 else low + 1

    for num in range(low, high + 1, 2):
        result += num

    return result

if __name__ == "__main__":
    print(sum_even_numbers(1, 100))