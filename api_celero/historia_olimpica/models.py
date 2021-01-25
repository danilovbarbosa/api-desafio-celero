from django.db import models

class AthleteEvents(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    age = models.IntegerField(null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    weight = models.FloatField(null=False, blank=False)
    team = models.CharField(max_length=100, null=False, blank=False)
    noc = models.CharField(max_length=3, null=False, blank=False)
    games = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    season = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    sport = models.CharField(max_length=100, null=False, blank=False)
    event = models.CharField(max_length=100, null=False, blank=False)
    medal = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.name




