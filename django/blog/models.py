from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

def get_name_file(instance, filename):
    strge = 'pictures/blog/' + str(instance.slug) + filename[-4:]
    return(strge)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Nadpis článku")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Neměnit!")
    body = models.TextField(verbose_name="Obsah článku")
    posted = models.DateField(db_index=True, auto_now_add=True)
    pic = ThumbnailerImageField(upload_to=get_name_file, null=True, blank=True, verbose_name="Titulní foto")

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
