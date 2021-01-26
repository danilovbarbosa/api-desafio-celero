from django.db import models

class NocRegions(models.Model):
    noc = models.CharField(max_length=3, null=False, blank=False)
    region = models.CharField(max_length=100, null=False, blank=False)
    notes = models.CharField(max_length=100, null=False, blank=False)


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
    noc = models.ForeignKey(NocRegions, on_delete=models.CASCADE, null=False, blank=False)
    games = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    season = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    sport = models.CharField(max_length=100, null=False, blank=False)
    event = models.CharField(max_length=100, null=False, blank=False)
    medal = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.name





