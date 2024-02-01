import mysql.connector
import pygame

class Affichage:
    def __init__(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='F1m13I12l5*', database='store')

        self.cursor = self.db.cursor()
