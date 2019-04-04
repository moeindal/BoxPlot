import csv
import matplotlib.pyplot as plt


def get_rating_list(product):
    with open("allCameras_editor_review.tsv") as allCameraReview:
        allCameraReview_reader = csv.reader(allCameraReview, delimiter="\t")
        temp_list = []
        for line in allCameraReview_reader:
            for l in product:
                print(l + '----' + line[0])
                if l in line[0]:
                    temp_list.append(float(line[1][15:18]))
                    print(l + ' --- ' + line[1][15:18])
    return temp_list


def get_product_id(modelName):
    with open("allCameras_spec.tsv") as allCameraSpec:
        allCameraSpec_reader = csv.reader(allCameraSpec, delimiter="\t")
        temp_list = []
        counter = -1
        for line in allCameraSpec_reader:
            if counter == 0:
                counter = counter + 1
                continue
            if line[1][:] == modelName:
                not_exist = True
                for newline in temp_list:
                    if newline == line[0][:]:
                        not_exist = False
                if not_exist:
                    temp_list.append(line[0][:])
            counter = counter + 1
    return temp_list


if __name__ == '__main__':
    temp = [get_rating_list(product=get_product_id('Sony')),
            get_rating_list(product=get_product_id('Canon')),
            get_rating_list(product=get_product_id('Olympus'))]
    plt.boxplot(temp)
    plt.show()
