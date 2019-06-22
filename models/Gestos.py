from mongoengine import *

class Gesto(Document):
    descripcion = StringField()
    inicio = ReferenceField('Vector')
    fin = ReferenceField('Vector')