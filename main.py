import math

def perfect_square(nr: int):
    if int(math.sqrt(nr)) == float(math.sqrt(nr)):
        return True
    return False

def verify_all_are_perfect_squares(lst: list[int]) -> bool:
    for nr in lst:
        if perfect_square(int(nr)) == False:
            return False
    return True

def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_are_perfect_squares(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result

def bit_counts(x: int):
    bits = int(0)
    while x:
        if x % 2 == 1:
            bits = bits + 1
        x = x // 2
    return bits

def verify_all_same_bit_counts(lst: list[int]) -> bool:
    bits = bit_counts(lst[0])
    for i in range(1, len(lst)):
        if bit_counts(lst[i]) != bits:
            return False
    return True

def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_same_bit_counts(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1,2,3,4,5]) == [1]
    assert get_longest_all_perfect_squares([1,4,9,3,7,4,9,16,25]) == [4,9,16,25]
    assert get_longest_all_perfect_squares([2,3,5,6,7,8]) == []

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([2, 4, 6, 7, 6, 8, 8, 3, 6, 10]) == [3, 6, 10]
    assert get_longest_same_bit_counts([35, 85, 69, 36, 85, 85, 45]) == [85, 85, 45]
    assert get_longest_same_bit_counts([]) == []

def main():
    while True:
        print("Optiuni:")
        print("1. Citeste o lista de numere de la tastatura")
        print("2. Determina cea mai lunga subsecventa cu toate elementele patrate perfecte")
        print("3. Determina cea mai lunga subsecventa cu toate elementele care au acelasi numar de biti 1 in reprezentarea binara")
        print("4. Termina programul")
        option = input("Scrie numarul aferent optiunii: ")

        if option == "1":
            n = input("Dati numarul de numere: ")
            print("Dati numerele:", end = " ")
            lst = list(map(int, input().split()))

        if option == "2":
            print("Cea mai lunga subsecventa cu toate numerele patrate perfecte este:", end = " ")
            print(get_longest_all_perfect_squares(lst))

        if option == "3":
            print("Cea mai lunga subsecventa cu toate elementele care au acelasi numar de biti 1 in reprezentarea binara este:" , end = " ")
            print(get_longest_same_bit_counts(lst))

        if option == "4":
            break
        print()

if __name__ == '__main__':

    test_get_longest_all_perfect_squares()
    test_get_longest_same_bit_counts()

    main()
    exit(0)