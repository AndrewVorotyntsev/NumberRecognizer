import os

import utils as utils

# x - inputs
# y - outputs
# w - weights
#


# Идея реализовать класс Learner. Его свойства - атрибуты: порог, темп обучения

def activate_neurons(z):
    for i in range(10):
        # Берем некоторый порог
        if z[i] > 5:
            z[i] = 1
        else:
            z[i] = 0
    return z


def calculate_errors(target, target_number, z):
    errors = []
    for i in range(len(target)):
        this_error = target[target_number][i] - z[i]
        errors.append(this_error)
    return errors


def calculate_new_weights(previous_weights, errors, x):
    new_weights = []
    for i in range(len(previous_weights)):
        new_weights.append([])
        for j in range(len(previous_weights[i])):
            this_new_weight = previous_weights[i][j] + errors[i] * 0.01 * x[j]
            new_weights[i].append(round(this_new_weight, 4))
    return new_weights


def learn(x):
    # Считываем веса
    weights = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")

    # Перемножение входных данных на веса
    z = utils.multiply_matrices(x, weights)

    # Функция активации
    z = activate_neurons(z)

    utils.show_neuron_reaction(z)

    # Расчет ошибок
    errors = calculate_errors(target, target_number, z)


    # Перерасчет весов
    new_weights = calculate_new_weights(weights, errors, x)

    # Запись новых весов
    utils.write_array_to_file_in_many_lines(new_weights, "weights.txt")

# Ввод целевого числа
target_number = int(input("Введите целевое число: "))
# Из введенного числа создается имя файла для входных данных

# Считываем входные данные

# Идея: реализовать полиморфизм для разных типов файлов

x = []

mode = input("Введите формат файла - txt или png ")
while mode is not True:
    # Путь до директории со скриптом
    main = os.path.dirname(__file__)
    file_name = str(target_number) + "." + mode
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

# Единичная матрица target
target = utils.create_identity_matrix(10)

# Количество эпох - итераций обучения
epoch = int(input("Введите число эпох: "))

# Процесс обучения
while epoch > 0:
    # Считываем веса
    weights = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")

    # Перемножение входных данных на веса
    z = utils.multiply_matrices(x, weights)

    # Функция активации
    z = activate_neurons(z)

    utils.show_neuron_reaction(z)

    # Расчет ошибок
    errors = calculate_errors(target, target_number, z)
    print(z, "Отреагировали ")

    print(errors, "Ошибки")
    # Перерасчет весов
    new_weights = calculate_new_weights(weights, errors, x)

    # Запись новых весов
    utils.write_array_to_file_in_many_lines(new_weights, "weights.txt")

    epoch = epoch - 1


# TODO: придумать демонстрацию изменений во време эпохи (надо ли ?)

# TODO: реализовать цикл прохода 1000 раз по каждой цифре
# Учим 1000 раз : выучи 1 один раз, выучи 2 один раз и т.д.
# Для того, чтобы сеть не зазубривала только одну цифру, забывая остальные
# Как вариант, под конец можно сделать не-обучение (это не 1, это не 2 и т.д)
