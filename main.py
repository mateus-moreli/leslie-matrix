import numpy as np

def informacoes():
    Ni = input("Entre com a população inicial por faixa etária\n")
    nasc = input("Entre com a quantidade de nascimentos por faixa etária: \n")
    sobrev = input("Entre com a quantidade de sobreviventes por faixa etária: \n")
    relatorio = open("relatorio.txt", "w")

    relatorio.write("A população inicial é: ")
    relatorio.write(Ni)
    relatorio.write("\n")

    relatorio.write("O número de nascimentos são: ")
    relatorio.write(nasc)
    relatorio.write("\n")

    relatorio.write("O número de individuos que chegam a proxima faixa etária são: ")
    relatorio.write(sobrev)
    relatorio.write("\n")
    relatorio.close()

    Ni_lista = list(map(int, Ni.split()))
    nasc_lista = list(map(float, nasc.split()))
    sobrev_lista = list(map(float, sobrev.split()))

    return Ni_lista, nasc_lista, sobrev_lista, relatorio

Ni, nasc, sobrev, relatorio = informacoes()


def taxas(Ni, nasc, sobrev):
    tx_nasc = []
    tx_sobrev = []

    for i in range(len(nasc)):
        tx = nasc[i] / Ni[i]
        tx_nasc.append(tx)

    for j, s in enumerate(sobrev):
        tx = s / Ni[j]
        tx_sobrev.append(tx)

    return tx_sobrev, tx_nasc

tx_sobrev, tx_nasc = taxas(Ni, nasc, sobrev)


def Matriz_de_leslie(tx_sobrev, tx_nasc):

    leslie = [[0 for j in range(len(Ni))] for i in range(len(Ni))]
    leslie[0] = tx_nasc
    for i in range(1, len(Ni)):
        leslie[i][i-1] = tx_sobrev[i-1]
    return leslie

def write_matrix_to_file(matrix):
    with open("relatorio.txt", 'a') as file:
        file.write("\n")
        file.write("A matriz de Leslie é: ")
        file.write("\n")
        for row in matrix:
            formatted_row = '\t'.join('{:.2f}'.format(cell) for cell in row)
            file.write(formatted_row + '\n')


matriz = Matriz_de_leslie(tx_sobrev, tx_nasc)

print(matriz)
def vidente(k, matriz, Ni):
    if k == 1:
        Ne = np.dot(matriz, Ni)
    else:
        Ne_prev = vidente(k - 1, matriz, Ni)
        Ne = np.dot(matriz, Ne_prev)
    return Ne

def write_array_to_file(array, file_path):
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a NumPy array.")
    elif array.ndim not in [1, 2]:
        raise ValueError("Input must be a 1-dimensional or 2-dimensional NumPy array.")
    if array.ndim == 1:
        array = array.reshape((1, array.shape[0]))
    with open(file_path, 'a') as file:
        file.write("\n")
        file.write("O vetor populacional desejado é: ")
        file.write("\n")
        for row in array:
            formatted_row = '\t'.join('{:.2f}'.format(cell) for cell in row)
            file.write(formatted_row + '\n')

def menu():
    resultado = None  # initialize resultado to None
    while True:
        a = input('Deseja calcular o vetor populacional? s/n \n')
        if a == 's':
            k = int(input("Entre com o número de anos que deseja prever a partir de hoje: "))
            resultado = vidente(k, matriz, Ni)
            write_array_to_file(resultado, "relatorio.txt")
            print(resultado)
        else:
            if resultado is not None:
                write_array_to_file(resultado, "relatorio.txt")
            break  # exit the while loop
     # write resultado to file
        relatorio.close()


write_matrix_to_file(matriz)
relatorio.close()
menu()
#k = int(input("Entre com o número de anos que deseja prever a partir de hoje: "))
#resultado = vidente(k, matriz, Ni)
#print(resultado)


