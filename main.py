import pygame
import socket

# Initialize PyGame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Connect to the server using sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.1', 5757))
