from PIL import Image, ImageFilter
import cv2
import time



imagen_jirafa = Image.open("/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/jirafa.png")
# imagen_jirafa.show()

# 500, 310

jirafa_recortada = imagen_jirafa.crop((0, 0, 500, 310))
# jirafa_recortada.show()

tamaño_jirafa_recortada = jirafa_recortada.size
print(tamaño_jirafa_recortada)

jirafa_recortada_mitad = jirafa_recortada.resize((int(tamaño_jirafa_recortada[0]/2), int(tamaño_jirafa_recortada[1]/2)))
# jirafa_recortada_mitad.show()


jirafa_espejo = jirafa_recortada_mitad.transpose(Image.FLIP_LEFT_RIGHT)
# jirafa_espejo.show()

# jirafa_espejo.convert("L").show()


imagen_jirafa = Image.open("/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/jirafa.png").resize((int(imagen_jirafa.size[0]/2), int(imagen_jirafa.size[1]/2)))
# imagen_jirafa.show()

imagen_contorneada = imagen_jirafa.filter(ImageFilter.CONTOUR)
# imagen_contorneada.show()

# Aplicar filtro de nitidez
imagen_nitidez = imagen_jirafa.filter(ImageFilter.SHARPEN)
# imagen_nitidez.show()

# Aplicar filtro de desenfoque
imagen_desenfocada = imagen_jirafa.filter(ImageFilter.BLUR)
# imagen_desenfocada.show()


imagen_jirafa = cv2.imread("/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/jirafa.png")

# cv2.imshow("Jirafa normal", imagen_jirafa)
# cv2.waitKey(0)

bordes_jirafa = cv2.Canny(imagen_jirafa, 100, 200)
# cv2.imshow("Jirafa bordes", bordes_jirafa)
# cv2.waitKey(0)

jirafa_desenfocada_cv1 = cv2.GaussianBlur(imagen_jirafa, (13, 13), 0)
# cv2.imshow('Jirafa Desenfoque 5x5 - OpenCV', jirafa_desenfocada_cv1)
# cv2.waitKey(0)

jirafa_desenfocada_cv2 = cv2.GaussianBlur(imagen_jirafa, (3, 3), 0)
# cv2.imshow('Jirafa Desenfoque 2x2 - OpenCV', jirafa_desenfocada_cv2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow('Original Jirafa - OpenCV' , imagen_jirafa)
cv2.waitKey(0)


kernel_cv = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

erosion_cv = cv2.erode(imagen_jirafa, kernel_cv, iterations=1)
# cv2.imshow('Erosión Jirafa - OpenCV' , erosion_cv)
# cv2.waitKey(0)

dilatacion_cv = cv2.dilate(imagen_jirafa, kernel_cv, iterations=1)
cv2.imshow('Dilatación Jirafa - OpenCV', dilatacion_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()