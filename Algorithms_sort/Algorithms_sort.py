import random

def generate(size):
    return [random.randint(-100, 100) for _ in range(size)]

def pop_sort(default_list):
    vec = default_list.copy()
    n = len(vec)
    count = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            count += 1
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

    print(f"Количество сравнений пузырьком: {count}")
    return vec

def insertion_sort(default_list):
    vec = default_list.copy()
    count = 0

    for i in range(1, len(vec)):
        key_value = vec[i]
        
        left = 0
        right = i
        while left < right:
            count += 1
            mid = (left + right) // 2
            if vec[mid] <= key_value:
                left = mid + 1
            else:
                right = mid
                
        vec.insert(left, key_value)
        vec.pop(i + 1)

    print(f"Количество сравнений вставками: {count}")
    return vec

def sort_for_hoar(vec, count):
    # Если массив пустой или из одного элемента
    if len(vec) <= 1:
        return vec

    pivot = vec[len(vec) // 2] # Выбираем опорный элемент
    left_part = []
    right_part = []
    equal_part = []

    for x in vec:
        count[0] += 1 # Считаем сравнения с опорным элементом
        if x < pivot:
            left_part.append(x)
        elif x > pivot:
            right_part.append(x)
        else:
            equal_part.append(x)

    # Рекурсивно сортируем левую и правую части и складываем
    return sort_for_hoar(left_part, count) + equal_part + sort_for_hoar(right_part, count)

def hoar_sort(default_list):
    vec = default_list.copy()
    count = [0]
    
    sorted_vec = sort_for_hoar(vec, count)

    print(f"Количество сравнений в методе Хоара: {count[0]}")
    return sorted_vec

def main():
    default_list = generate(10)
    print("Исходный массив:", default_list)
    print("\n")

    print("Сортировка пузырьком:")
    pop_sorted_vector = pop_sort(default_list)
    print("Отсортированный массив:", pop_sorted_vector)
    print("\n")

    print("Сортировка вставками (бинарный поиск + insert):")
    insert_sorted_vector = insertion_sort(default_list)
    print("Отсортированный массив:", insert_sorted_vector)
    print("\n")

    print("Сортировка методом Хоара (с созданием новых массивов):")
    hoar_sorted_vector = hoar_sort(default_list)
    print("Отсортированный массив:", hoar_sorted_vector)
    print("\n")

if __name__ == "__main__":
    main()