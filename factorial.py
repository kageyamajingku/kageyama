def factorial(n):
    """
    Menghitung faktorial dari bilangan n secara rekursif.
    :param n: int - Bilangan input (harus >= 0)
    :return: int - Faktorial dari n
    """
    if n < 0:
        raise ValueError("Bilangan harus lebih besar atau sama dengan 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Masukkan bilangan: "))
        print(f"Faktorial dari {number} adalah {factorial(number)}")
    except ValueError as e:
        print(f"Error: {e}")
