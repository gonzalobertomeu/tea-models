from mongoengine import *

class Estudio(Document):
    fecha = DateTimeField()
    descripcion = StringField()
    usuario = ReferenceField('Usuario')
    medico = ReferenceField('Medico')
    video = ReferenceField('Video')
    gestos = ListField(ReferenceField('Gesto'))
    