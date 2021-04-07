import csv
from graph import ColoredGraph


def main():
    with open('shapefiles/province_names.txt', 'r') as f:
        province_names = f.read().splitlines()

    with open('shapefiles/incedence_matrix.csv', 'r', newline='') as f:
        matrix = [[int(x) for x in row] for row in csv.reader(f)]

    spain = ColoredGraph(matrix)
    colors = spain.get_colors()

    print_colors(colors, province_names)
    print('Хроматичне число:', spain.chromatic_number)


def print_colors(colors: list[int], names: list[str]):
    for name, color in zip(names, colors):
        print(f'Область {name}', '–'.rjust(19 - len(name)), f'Колір {color}')

if __name__ == '__main__':
    main()