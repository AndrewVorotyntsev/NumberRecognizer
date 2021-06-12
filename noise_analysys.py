import random
import os
import utils
import matplotlib.pyplot as plt


def make_noise(data_to_noise, amount_of_noisy_elements):
    indexes = [i for i in range(0, len(data_to_noise))]
    elements_to_noise = random.sample(indexes, k=amount_of_noisy_elements)
    for i in elements_to_noise:
        data_to_noise[i] = abs(data_to_noise[i] - 1)
    return data_to_noise


def activate_neurons(z):
    for i in range(10):
        # Берем некоторый порог
        if z[i] > 5:
            z[i] = 1
        else:
            z[i] = 0
    return z


# Ввод целевого образа
target_number = int(input("Введите целевое число: "))
# Считываем входные данные
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

# Считываем веса
weights = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")

stat = []

for i in range(0,5):

    a = 1000

    this_stat = 0

    while a > 0:

        x = make_noise(x, i)

        # Перемножение входных данных на веса
        z = utils.multiply_matrices(x, weights)

        # Функция активации
        z = activate_neurons(z)

        # Функция отображения результата работы нейронов
        reacted_neurons = utils.show_neuron_reaction(z)

        print("rn", reacted_neurons)

        # Второй варинт: если среагировал только нужный нейрон
        if reacted_neurons != [target_number]:
            this_stat = this_stat + 1

        a = a - 1

    print(this_stat)
    stat.append(this_stat)
    print(stat)

print(stat)

plt.plot(range(0,5),stat)
plt.show()
