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
        j = i - 1

        while j >= 0:
            count += 1
            if vec[j] > key_value:
                vec[j + 1] = vec[j]
                j -= 1
            else:
                break
        vec[j + 1] = key_value

    print(f"Количество сравнений вставками: {count}")
    return vec

def sort_for_hoar(vec, left, right, count):
    i = left
    j = right

    pivot = vec[(left + right) // 2]

    while i <= j:
        while vec[i] < pivot:
            count[0] += 1
            i += 1

        while vec[j] > pivot:
            count[0] += 1
            j -= 1

        if i <= j:
            vec[i], vec[j] = vec[j], vec[i]
            i += 1
            j -= 1

    if left < j:
        sort_for_hoar(vec, left, j, count)
    if i < right:
        sort_for_hoar(vec, i, right, count)

def hoar_sort(default_list):
    vec = default_list.copy()
    count = [0]
    sort_for_hoar(vec, 0, len(vec) - 1, count)

    print(f"Количество сравнений в методе Хоара: {count[0]}")
    return vec

def main():
    default_list = generate(10)
    print("Исходный массив:", default_list)
    print("\n")

    print("Сортировка пузырьком:")
    pop_sorted_vector = pop_sort(default_list)
    print("Отсортированный массив:", pop_sorted_vector)
    print("\n")

    print("Сортировка вставками:")
    insert_sorted_vector = insertion_sort(default_list)
    print("Отсортированный массив:", insert_sorted_vector)
    print("\n")

    print("Сортировка методом Хоара:")
    hoar_sorted_vector = hoar_sort(default_list)
    print("Отсортированный массив:", hoar_sorted_vector)
    print("\n")

if __name__ == "__main__":
    main()

