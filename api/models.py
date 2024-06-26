from django.db import models
from string import ascii_uppercase
from random import choices


def generate_unique_code():
    """Generates random code for the room model"""
    length = 6
    while True:
        code = "".join(choices(ascii_uppercase, k=length))
        # Verify if it's unique
        if Room.objects.filter(code=code).count == 0:
            break
    return code


# Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=8, unique=True, default="")
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
