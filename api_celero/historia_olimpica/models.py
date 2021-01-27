from django.db import models

class NocRegions(models.Model):
    noc = models.CharField(max_length=5, null=True, blank=True)
    region = models.CharField(max_length=150, null=True, blank=True)
    notes = models.CharField(max_length=150, null=True, blank=True)


class AthleteEvents(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    team = models.CharField(max_length=150, null=False, blank=False)
    noc = models.ForeignKey(NocRegions, on_delete=models.CASCADE, null=True, blank=True)
    games = models.CharField(max_length=150, null=False, blank=False)
    year = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=150, null=False, blank=False)
    city = models.CharField(max_length=150, null=False, blank=False)
    sport = models.CharField(max_length=150, null=False, blank=False)
    event = models.CharField(max_length=150, null=False, blank=False)
    medal = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.name





