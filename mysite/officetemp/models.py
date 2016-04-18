from django.db import models

# Create your models here.
class Temperature(models.Model):
    degrees = models.IntegerField(default=70)
    def __str__(self):              # __unicode__ on Python 2
        return self.degrees

    def display_room_condition(self):
        if self.degrees > 72:
            room_condition = "hot"
        elif self.degrees < 68:
            room_condition = "cold"
        else:
            room_condition = "comfy"
        return room_condition
