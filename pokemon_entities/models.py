from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField('Имя',max_length=200, default="")
    image = models.ImageField('Картинка', default="")
    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

