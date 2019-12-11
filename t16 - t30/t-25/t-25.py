import cv2 as cv
import numpy as np
from numba import njit

seed = (0, 0)
count = 0

@njit
def regiongrowing(img, img_selected, seed=None):

    # getting the img dimensions
    rows, cols = img.shape[:2]

    # variables for loop
    current_point = 0
    previous_point = 1

    while previous_point != current_point:

        previous_point = current_point
        current_point = 0

        for row in range(rows):
            for col in range(cols):

                # we will set for each object on pixel value for identification of that

                # growing the first object
                if img_selected[row, col] == 1:
                    if img[row - 1, col -1] < 230:
                        img_selected[row - 1, col - 1] = 1
                        current_point += 1
                    if img[row - 1, col] < 230:
                        img_selected[row - 1, col] = 1
                        current_point += 1
                    if img[row -1, col + 1] < 230:
                        img_selected[row - 1, col + 1] = 1
                        current_point += 1
                    if img[row, col -1] < 230:
                        img_selected[row, col - 1] = 1
                        current_point += 1
                    if img[row, col + 1] < 230:
                        img_selected[row, col + 1] = 1
                        current_point += 1
                    if img[row + 1, col -1] < 230:
                        img_selected[row + 1, col - 1] = 1
                        current_point += 1
                    if img[row + 1, col] < 230:
                        img_selected[row + 1, col] = 1
                        current_point += 1
                    if img[row + 1, col + 1] < 230:
                        img_selected[row + 1, col + 1] = 1
                        current_point += 1

                # growing the second object
                if img_selected[row, col] == 2:
                    if img[row - 1, col -1] < 230:
                        img_selected[row - 1, col - 1] = 2
                        current_point += 1
                    if img[row - 1, col] < 230:
                        img_selected[row - 1, col] = 2
                        current_point += 1
                    if img[row -1, col + 1] < 230:
                        img_selected[row - 1, col + 1] = 2
                        current_point += 1
                    if img[row, col -1] < 230:
                        img_selected[row, col - 1] = 2
                        current_point += 1
                    if img[row, col + 1] < 230:
                        img_selected[row, col + 1] = 2
                        current_point += 1
                    if img[row + 1, col -1] < 230:
                        img_selected[row + 1, col - 1] = 2
                        current_point += 1
                    if img[row + 1, col] < 230:
                        img_selected[row + 1, col] = 2
                        current_point += 1
                    if img[row + 1, col + 1] < 230:
                        img_selected[row + 1, col + 1] = 2
                        current_point += 1

                # growing the third object
                if img_selected[row, col] == 3:
                    if img[row - 1, col -1] < 230:
                        img_selected[row - 1, col - 1] = 3
                        current_point += 1
                    if img[row - 1, col] < 230:
                        img_selected[row - 1, col] = 3
                        current_point += 1
                    if img[row -1, col + 1] < 230:
                        img_selected[row - 1, col + 1] = 3
                        current_point += 1
                    if img[row, col -1] < 230:
                        img_selected[row, col - 1] = 3
                        current_point += 1
                    if img[row, col + 1] < 230:
                        img_selected[row, col + 1] = 3
                        current_point += 1
                    if img[row + 1, col -1] < 230:
                        img_selected[row + 1, col - 1] = 3
                        current_point += 1
                    if img[row + 1, col] < 230:
                        img_selected[row + 1, col] = 3
                        current_point += 1
                    if img[row + 1, col + 1] < 230:
                        img_selected[row + 1, col + 1] = 3
                        current_point += 1

    return img_selected

def clickmouse(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDOWN:
        global seed
        global count
        global img_selected

        count += 1

        img_selected[y, x] = count


if __name__ == '__main__':
    # reading the image and converting to gray scale
    img = cv.imread("/home/andre/Área de Trabalho/training/codigos/t-25/forms.png", 1)

    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # setting one matrix to 'save' the area for the segmentation
    img_selected = np.zeros_like(img)

    # showing the window to wait the click
    cv.namedWindow("loaded-image", 1)
    cv.imshow("loaded-image", img)
    cv.setMouseCallback("loaded-image", clickmouse)
    cv.waitKey(0)

    # apply the region-growing
    segmented = regiongrowing(img, img_selected)

    # creating a RGB image for the segmented
    rows, cols = segmented.shape[:2]
    new = np.zeros([rows, cols, 3], np.uint8)

    # coloring the marked pixel of the objects
    new[np.where(segmented == 1)] = [0, 0, 255]
    new[np.where(segmented == 2)] = [255, 0, 0]
    new[np.where(segmented == 3)] = [0, 255, 0]

    cv.imshow("segmented", new)
    cv.waitKey(0)
   # print(new)
    cv.imwrite("result.jpg",new)


