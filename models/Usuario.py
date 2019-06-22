from mongoengine import *

class Usuario(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    dni = StringField(required=True)
    edad = IntField(required=True)
    sexo = StringField(required=True)