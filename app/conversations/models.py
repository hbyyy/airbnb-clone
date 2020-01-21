from django.db import models
from core import models as core_models

# Create your models here.


class Conversations(core_models.TimeStampedModel):
    """Conversations Model Definition"""
    participants = models.ManyToManyField('users.User', blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    Conversations = models.ForeignKey('Conversations', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'
