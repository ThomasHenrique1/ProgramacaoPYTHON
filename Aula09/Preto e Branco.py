import cv2
cinza = True
image = cv2.imread('riuori.jpg')
# função ue converte img color em cinza
if(cinza == True):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Imagem em Tons de Cinza", gray)
    cv2.imshow("Imagem Preto e Branco", bw)
    cv2.imshow("Imagem Colorida", image)
    cv2.imwrite("resultado.jpg", image)
cv2.waitKey(0)