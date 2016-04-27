from django.db import models


class Ambito(models.Model):
    num = models.SmallIntegerField(unique=True)
    descrizione = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Ambiti"

    def __str__(self):
        return self.descrizione


class Tag(models.Model):
    descrizione = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['descrizione']

    def __str__(self):
        return self.descrizione


class Spesa(models.Model):
    data_accredito = models.DateField()
    data_riferimento = models.DateField()
    importo = models.DecimalField(max_digits=15, decimal_places=2)
    # la descrizione finora viene usata con lunghezza max = 275
    descrizione = models.CharField(max_length=300)
    quantita = models.SmallIntegerField()
    ambito = models.ForeignKey('Ambito')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name_plural = "Spese"

    def __str__(self):
        return self.descrizione
