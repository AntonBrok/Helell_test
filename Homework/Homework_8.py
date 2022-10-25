from random import randint

numbers = []
for i in range(20):
    numbers.append(randint(1, 10))
print("Числа: ", numbers)


def numbers_count(sequence: list) -> dict:
    result = {}
    for item in sequence:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


result = numbers_count(numbers)
for item in result:
    print(f"Число {item} встречаеться : "
          f"{result[item]} раз")