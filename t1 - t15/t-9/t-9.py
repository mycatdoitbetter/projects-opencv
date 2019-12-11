import cv2 as cv
from PIL import Image
## tucano tem 1277x912 pixels

img = cv.imread('tucano.jpg',0)
# objeto px_im sendo aberto com a biblioteca PIL.Image, o objeto vai conter o BRG de cada pixel
# lido, ou seja, serão 12277*912*3 numeros.
px_im = Image.open('tucano.jpg','r')
# criando lista a partir da informação do image.open em txt
px_val = list(px_im.getdata())

#abrindo arquivo onde seram guardadas as informações
matrix = open('matrix.txt','w+')

# a lista criada acima, esta em forma de triplas, o algoritimo abaixo transforma em uma lista flat
px_val_flat = [x for sets in px_val for x in sets]

# transformando os inteiros da lista em str e adicionando espaço entre os elementos, assim como
# adicionando ao documento matrix
for i in range(len(px_val_flat)):
    px_val_flat[i] = str(px_val_flat[i])+' '

    matrix.write(px_val_flat[i])


cv.waitKey()