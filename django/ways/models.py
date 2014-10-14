# POZOR! Vysouvací menu není dynamicky vytvářeno (nastavuje se pevně v base.html)

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


def get_name_file(instance, filename):
    strge = ""
    if filename[-4] == ".":
        strge = 'pictures/ways/pics/' + str(instance.slug) + filename[-4:]
    else:
        strge = 'pictures/ways/pics/' + str(instance.slug) + ".png"
    return(strge)


class Way(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(verbose_name="Popis stezky obecně")
    marks = models.CharField(max_length=100, verbose_name='Značka')
    the_path = models.TextField(verbose_name="Popis trasy", null=True, blank=True)
    length = models.SlugField(max_length=100, verbose_name="Délka")

    interest1_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Název zajímavosti 1")
    interest1_body = models.TextField(null=True, blank=True, verbose_name="Popis zajímavosti 1")
    interest2_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Název zajímavosti 2")
    interest2_body = models.TextField(null=True, blank=True, verbose_name="Popis zajímavosti 2")
    interest3_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Název zajímavosti 3")
    interest3_body = models.TextField(null=True, blank=True, verbose_name="Popis zajímavosti 3")

    map_of_way = ThumbnailerImageField(upload_to='pictures/ways/maps', null=True, blank=True)

    pic1 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True, verbose_name = "Titulní foto")
    picd_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic2 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic3 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic4 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_4 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic5 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_5 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic6 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_6 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic7 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_7 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")
    pic8 = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True)
    picd_8 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Popis")

    def __str__(self):
        return self.title