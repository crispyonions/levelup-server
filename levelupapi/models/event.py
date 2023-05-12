from django.db import models
from levelupapi.models import Gamer, Game

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField(Gamer, related_name="attended_events")

