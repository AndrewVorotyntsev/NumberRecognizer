from PIL import Image


def read_file_to_one_dimensional_array_of_ints(file_name):
    print(file_name)
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            for x in line.split():
                array_to_write.append(float(x))
    return array_to_write


def read_file_to_one_dimensional_array_of_floats(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            for x in line.split():
                array_to_write.append(float(x))
    return array_to_write


def read_file_to_two_dimensional_array_of_ints(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            array_to_write.append([int(x) for x in line.split()])
    return array_to_write


def read_file_to_two_dimensional_array_of_floats(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            array_to_write.append([float(x) for x in line.split()])
    return array_to_write


def write_array_to_file_in_one_line(array_to_read, file_name):
    file_name = open(file_name, "w")
    one_line = ""
    for i in range(len(array_to_read)):
        for j in range(len(array_to_read[i])):
            one_line = one_line + str(array_to_read[i][j]) + " "
        file_name.write(one_line)


def write_array_to_file_in_many_lines(array_to_read, file_name):
    file_to_write = open(file_name, "w")
    for i in range(len(array_to_read)):
        # Для загрузки в несколько строк объявляем переменную строки после запуска цикла
        line = ""
        for j in range(len(array_to_read[i])):
            line = line + str(array_to_read[i][j]) + " "
        line = line.strip(" ") + "\n"
        file_to_write.write(line)


def create_identity_matrix(dimension):
    matrix = []
    for i in range(dimension):
        matrix.append([])
        for j in range(dimension):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


def multiply_matrices(a, b):
    result = []
    res = 0
    for i in range(len(b)):
        for j in range(len(a)):
            res = res + a[j]*b[i][j]
        result.append(round(res, 4))
        res = 0
    return result


def show_neuron_reaction(z):
    reacted_neurons = []
    for i in range(len(z)):
        if z[i] == 1:
            reacted_neurons.append(i)
            print("Отреагировал нейрон", i)
    return reacted_neurons

def create_matrix_of_pixels(w):
    q = []
    for i in range(len(w)):
        q.append([])
        n = 0
        for j in [0, 5, 10, 15, 20, 25, 30]:
            q[i].append([])
            q[i][n].append(w[i][j])
            q[i][n].append(w[i][j+1])
            q[i][n].append(w[i][j+2])
            q[i][n].append(w[i][j+3])
            q[i][n].append(w[i][j+4])
            n = n + 1
    w = q
    return w


def convert_image_into_array(image_file):
    image = Image.open(image_file)
    gray = image.convert('L')
    bw = gray.point(lambda x: 0 if x > 128 else 1, '1')
    data = list(bw.getdata())
    return data
