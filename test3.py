n = [1, 2, 3, 7, 5]

def sort_list(numbers):
    result = []
    b=numbers[0]
    for item in numbers:
        if item >= b:
            result.append(item)
            b=item
    return result

print sort_list(n)
