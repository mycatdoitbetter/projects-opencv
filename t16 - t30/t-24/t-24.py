import cv2
import numpy as np

semente = (0, 0)

def crescimento_regioes(imagem, semente=None):
    rows, cols = imagem.shape[:2]

    xc, yc = semente

    ref_cor = imagem[xc, yc]

    segmentado = np.zeros_like(imagem)

    segmentado[xc, yc] = ref_cor

    ponto_atual = 0
    ponto_anterior = 1

    while ponto_anterior != ponto_atual:

        ponto_anterior = ponto_atual
        ponto_atual = 0
        for row in range(rows):
            for col in range(cols):

                if np.array_equal(segmentado[row, col], ref_cor):
                    if np.array_equal(imagem[row - 1, col - 1], ref_cor):
                        segmentado[row - 1, col - 1] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row - 1, col], ref_cor):
                        segmentado[row - 1, col] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row - 1, col + 1], ref_cor):
                        segmentado[row - 1, col + 1] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row, col - 1], ref_cor):
                        segmentado[row, col - 1] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row, col + 1], ref_cor):
                        segmentado[row, col + 1] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row + 1, col - 1], ref_cor):
                        segmentado[row + 1, col - 1] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row + 1, col], ref_cor):
                        segmentado[row + 1, col] = ref_cor
                        ponto_atual += 1
                    if np.array_equal(imagem[row + 1, col + 1], ref_cor):
                        segmentado[row + 1, col + 1] = ref_cor
                        ponto_atual += 1

        cv2.imshow('img-segmentada', segmentado)
        cv2.waitKey(1)

    return segmentado

def clique_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        global semente

        semente = (y, x)


if __name__ == '__main__':

    img = cv2.imread('/home/andre/Área de Trabalho/training/codigos/t-24/rgb.jpg')

    img_rgb = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

    cv2.namedWindow('img-rgb', 1)
    cv2.imshow('img-rgb', img_rgb)
    cv2.setMouseCallback('img-rgb', clique_mouse)
    cv2.waitKey(0)

    img_segmentada = crescimento_regioes(img_rgb, semente)


    cv2.imshow('img-segmentada', img_segmentada)
    cv2.waitKey(0)

    cv2.imwrite('img-segmentada.jpg', img_segmentada)