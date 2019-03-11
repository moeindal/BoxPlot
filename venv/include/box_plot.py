import csv
import matplotlib.pyplot as plt

def create_box_plot():
    with open("allCameras_editor_review.tsv") as tsvFile:
        tsv_reader = csv.reader(tsvFile, delimiter="\t")

        temp_list = []
        counter = -1
        for line in tsv_reader:
            #First Line In tsv_reader Is Titles So We Must Ignore This Line And Use Other Lines For Create Box Plot
            if counter == 0:
                counter = counter + 1
                continue

            if line[1][15:18] != '':
                # Every Rating Filed Has Some Text And A Rate Number, We Just Need The Number
                temp_list.append(float(line[1][15:18]))
            counter = counter + 1

        plt.boxplot(temp_list)
        plt.show()


if __name__ == '__main__':
    create_box_plot()
