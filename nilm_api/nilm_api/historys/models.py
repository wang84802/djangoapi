from django.db import models


class PowerStatisticsDay(models.Model):
    date = models.DateField()
    device = models.CharField(max_length=100, db_collation='utf8_general_ci')
    active = models.FloatField(blank=True, null=True)
    reactive = models.FloatField(blank=True, null=True)
    apparent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'power_statistics_day'