import csv
import matplotlib.pyplot as plt


def create_box_plot():
    with open("allCameras_editor_review.tsv") as tsvFile:
        tsv_reader = csv.reader(tsvFile, delimiter="\t")
        temp_array = []
        l = -1
        for line in tsv_reader:
            if l == 0:
                l = l + 1
                continue
            if line[1][15:18] != '':
                temp_array.append(float(line[1][15:18].replace(',', '')))
            l = l + 1

        plt.boxplot(temp_array)
        plt.show()


if __name__ == '__main__':
    create_box_plot()
