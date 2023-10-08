numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_el = numbers.index(None)
sum_numbers = sum(numbers[:index_missing_el] + numbers[index_missing_el+1:])
numbers[index_missing_el] = sum_numbers / len(numbers)

print("Измененный список:", numbers)
