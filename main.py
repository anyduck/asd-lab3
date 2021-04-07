import csv
from graph import ColoredGraph


def main():
    with open('shapefiles/province_names.txt', 'r') as f:
        names = f.read().splitlines()

    with open('shapefiles/incedence_matrix.csv', 'r', newline='') as f:
        matrix = [[int(x) for x in row] for row in csv.reader(f)]

    spain = ColoredGraph(matrix)
    colors = spain.get_colors()

if __name__ == '__main__':
    main()