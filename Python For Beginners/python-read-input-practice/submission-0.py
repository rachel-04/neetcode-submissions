def add_two_numbers() -> int:
    line = input()
    numbers = line.split(",")
    result = []
    for num in numbers:
        result.append(int(num))
    results = result[0]+result[1]
    return results


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
