from django.db import models

# Create your models here. Aina kun teet täällä muutoksia niin luo uusi migraatio komennoilla:
# python manage.py makemigrations
# python manage.py migrate
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()
    kuva = models.ImageField(upload_to="blogi/kuvat", null=True, blank=True) #null=True = tietokanta voi olla ilman kuvaa, djnago admin tarvitsee lisäksi että kenttä saa jäädä tyhjäksi -> blank=True
    luotu = models.DateTimeField(auto_now_add = True) #pvm ja ajan tallentamista, milloin luotu.

    def __str__(self):
        return self.otsikko