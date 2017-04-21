import pygame
import pygame.camera
pygame.camera.init()

class Camara:
	tam = (320, 240)

	def __init__(self):
		print "incio capturador"
		camaras = pygame.camera.list_cameras()
		self.cam = pygame.camera.Camera(camaras[0], self.tam, "YUV")
		#self.cam.set_controls(True, False, 0)

	def detener(self):
		self.cam.stop()

	def iniciar(self):
		self.cam.start()

	def fotoXO(self):
		"""Toma una foto y devuelve la surface"""
		try:
			imageP = self.cam.get_image()
			self.image = pygame.transform.flip(imageP, True, False)
		except:
			pass
		return self.image