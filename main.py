#Функция заполнения списка
def enter_list():
    list_lines = []
    for _ in range(5):
        list_lines.append(input("Введите строку "))
    return list_lines


def swap_place(list_lines):
    first_line = list_lines[0]
    list_lines[0] = list_lines[4]
    list_lines[4] = first_line
    return list_lines


#Основное тело программы
print("Измененный список ", swap_place(enter_list()))