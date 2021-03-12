import os
import utils


def activate_neurons(z):
    for i in range(10):
        # Берем некоторый порог
        if z[i] > 5:
            z[i] = 1
        else:
            z[i] = 0
    return z


# Ввод целевого образа
target_image = input("Введите целевой образ: ")

# Считываем входные данные
x = []
mode = input("Введите формат файла - txt или png ")
while mode is not True:
    # Путь до директории со скриптом
    main = os.path.dirname(__file__)
    file_name = str(target_image) + "." + mode
    # Формируем путь до файла
    file_path = os.path.join(main, "templates", file_name)
    # Первый вариант: считывание из текстового файла
    if mode == "txt":
        x = utils.read_file_to_one_dimensional_array_of_ints(file_path)
        mode = True
    # Второй вариант: считывание из изображения
    elif mode == "png":
        x = utils.convert_image_into_array(file_path)
        mode = True
    else:
        mode = input("Неподходящий формат!\nВведите формат файла - txt или png ")

# Считываем веса
weights = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")

# Перемножение входных данных на веса
z = utils.multiply_matrices(x, weights)

# Функция активации
z = activate_neurons(z)

# Функция отображения результата работы нейронов
utils.show_neuron_reaction(z)
