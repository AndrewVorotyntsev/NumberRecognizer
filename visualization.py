# Отображение матрицы весов в виде heatmap

import matplotlib.pyplot as plot
import seaborn as sns
import utils as utils


# Считываем веса
weights = utils.read_file_to_two_dimensional_array_of_floats("weights.txt")

# Преобразуем матрицу весов в формат 10x7x5
weights = utils.create_matrix_of_pixels(weights)

# Массив для графиков
heat_maps = []

for i in range(len(weights)):
    plot.figure()
    heat_maps.append(sns.heatmap(weights[i], cmap="YlGnBu"))
    plot.title(str(i))

plot.show()
