from mongoengine import *

class Frame(Document):
    nFrame = IntField(required=True)
    image = FileField()
    video = ReferenceField('Video')
    vectores = SortedListField(ReferenceField('Vector'))