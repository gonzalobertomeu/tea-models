from mongoengine import *

class Video(Document):
    cantFrames = IntField(require=True)