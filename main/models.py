from django.db import models


class points_model(models.Model):
    user = models.CharField(max_length=20, primary_key=True)
    points = models.SmallIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user
        
class donate_model(models.Model):
    dollars = models.SmallIntegerField()
    