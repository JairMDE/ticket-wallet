from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import base64
import pytesseract

class Img2Text():
	"""docstring for ClassName"""
	def __init__(self, base64str):
		self.base64str = base64str

	def base64aimg(self):
		b64bytes = base64.b64decode(self.base64str)
		imagen_archivo = BytesIO(b64bytes)
		imagen = Image.open(imagen_archivo)
		return imagen

	def procesar_imagen(self, imagen):
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

		# retornarla si prefieres trabajar con ella directamente
		return imagen_procesada

	def mejorar_calidad_letras(self, imagen):
	    # Cargar la imagen
		array_imagen = np.array(imagen)
		imagen_cv2 = cv2.cvtColor(array_imagen, cv2.COLOR_RGB2BGR)
	    # Aplicar un filtro Gaussiano para suavizar la imagen
		imagen_umbralizada = cv2.GaussianBlur(imagen_cv2, (5, 5), 0)

	    # Umbralizar la imagen para obtener una imagen binaria
	    #_, imagen_umbralizada = cv2.threshold(imagen_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	    # Utilizar dilatación seguida de erosión para mejorar las letras
		kernel = np.ones((1, 1), np.uint8)
		imagen_umbralizada = cv2.dilate(imagen_umbralizada, kernel, iterations=1)

		# Guardar la imagen mejorada
		return imagen_umbralizada

	def imgatexto(self, imagen):
		imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
		texto = pytesseract.image_to_string(imagen_rgb)
		return texto
