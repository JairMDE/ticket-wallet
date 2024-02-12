import cv2 
import numpy as np 


def procesar_imagen(image_path):
# Lee la imagen 
    image = cv2.imread(image_path)


    # Se reajusta la imagen para un tamaño más estadar
    resized_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Se convierte a escalas de grises
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    #Gaussiano para suavizar la imáge
    #blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Se hace un denoising 
    denoised_image = cv2.fastNlMeansDenoising(gray_image, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # Se hace un treshold adaptativo a la imagen sin ruido previo
    threshold_image = cv2.adaptiveThreshold(denoised_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Ya que la imagen es binaria, se tienen que buscar los contornos
    contours, hierarchy = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Obten solo el contorno que nos interesa (asumiendo que es el recibo)
    largest_contour = max(contours, key=cv2.contourArea)

    # Crea una máscara a la imagen del mismo tamaño
    mask = np.zeros_like(threshold_image)

    # El contorno extraido lo crea en la máscara
    cv2.drawContours(mask, [largest_contour], 0, (255), thickness=cv2.FILLED)

    # Aplica el contorno a la imágen original 
    masked_image = cv2.bitwise_and(resized_image, resized_image, mask=mask)

    return masked_image

image_paths = ["/Users/jairmartinez/Documents/IoT Project/IoT-doctr/images/ticket-1.jpeg", 
               "/Users/jairmartinez/Documents/IoT Project/IoT-doctr/images/ticket-2.jpeg"]

for image_path in image_paths:
    processed_image = procesar_imagen(image_path)
    cv2.imshow('Imagen_procesada', processed_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

