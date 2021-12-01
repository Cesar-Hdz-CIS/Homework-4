# Cesar Hernandez
# 1835494

def selection_sort_descend_trace(numbers):
    for index in range(len(numbers) - 1):
        largest_index = index
        for n in range(index + 1, len(numbers)):
            if numbers[n] > numbers[largest_index]:
                largest_index = n
        numbers[index], numbers[largest_index] = numbers[largest_index], numbers[index]
        print(' '.join([str(x) for x in numbers]), "")
    return numbers

if __name__ == '__main__':
    number_list = [int(value) for value in input().split()]
    selection_sort_descend_trace(number_list)