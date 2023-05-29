from django.db import models


class Sensor(models.Model):
    datetime = models.DateTimeField()
    device = models.CharField(max_length=100)
    vo = models.FloatField()
    cu = models.FloatField()
    active = models.FloatField()
    reactive = models.FloatField()
    apparent = models.FloatField()
    pf = models.FloatField()
    freq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sensor'