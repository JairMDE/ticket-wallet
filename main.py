from PIL import Image
import numpy as np



import cv2
import numpy as np

def mejorar_calidad_letras(nombre_imagen_entrada, nombre_imagen_salida):
    # Cargar la imagen
    imagen = cv2.imread(nombre_imagen_entrada, cv2.IMREAD_GRAYSCALE)

    # Aplicar un filtro Gaussiano para suavizar la imagen
    imagen_umbralizada = cv2.GaussianBlur(imagen, (5, 5), 0)

    # Umbralizar la imagen para obtener una imagen binaria
    #_, imagen_umbralizada = cv2.threshold(imagen_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Utilizar dilatación seguida de erosión para mejorar las letras
    kernel = np.ones((1, 1), np.uint8)
    imagen_umbralizada = cv2.dilate(imagen_umbralizada, kernel, iterations=1)
    #imagen_mejorada = cv2.erode(imagen_umbralizada, kernel, iterations=1)

    # Guardar la imagen mejorada
    cv2.imwrite(nombre_imagen_salida, imagen_umbralizada)

    return nombre_imagen_salida





def procesar_imagen(ruta_imagen):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    # Convertir la imagen a escala de grises
    imagen_gris = imagen.convert('L')
    # Convertir la imagen a un array de numpy para procesarla
    datos = np.array(imagen_gris)
    
    # Definir el umbral para los píxeles oscuros (ajusta este valor según necesites)
    umbral_oscuro = 130  # Los píxeles con un valor menor a este se consideran oscuros

    # Usar una operación vectorizada para establecer todos los píxeles fuera del rango a blanco
    # y conservar los demás como están
    datos_procesados = np.where(datos < umbral_oscuro, datos, 255)

    # Convertir el array de vuelta a una imagen de Pillow
    imagen_procesada = Image.fromarray(datos_procesados.astype('uint8'), 'L')

    # Guardar la imagen procesada o retornarla
    imagen_procesada.save('imagen_procesada.jpg')
    # O retornarla si prefieres trabajar con ella directamente
    # return imagen_procesada





# Reemplaza 'ruta_a_tu_imagen.jpg' con la ruta a tu imagen
procesar_imagen('t.jpeg')

#mejorar_calidad_letras('t.jpeg', 'img_mejorada.jpg')
mejorar_calidad_letras('imagen_procesada.jpg', 'img_mejorada.jpg')
