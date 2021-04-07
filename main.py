import csv


def main():
    with open('shapefiles/province_names.txt', 'r') as f:
        names = f.read().splitlines()

    with open('shapefiles/incedence_matrix.csv', 'r', newline='') as f:
        matrix = [[int(x) for x in row] for row in csv.reader(f)]


if __name__ == '__main__':
    main()