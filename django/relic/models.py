from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

def get_name_file(instance, filename):
    strge = 'pictures/relics/' + str(instance.slug) + filename[-4:]
    return(strge)

types_choice = (       # example of 1, there can be only one selection
        ('Křížek', 'Křížek'),
        ('Socha', 'Socha'),
        ('Jiné', 'Jiné')
    )

class Relic(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Název")
    
    place = models.CharField(max_length=100, blank=True, verbose_name="Umístění")
    gps = models.CharField(max_length=50, blank=True, verbose_name="GPS")
    date_of_build = models.CharField(max_length=20, null=True, verbose_name="Datum vzniku", blank=True)
    reconstruction = models.CharField(max_length=200, null=True, verbose_name="Rekonstrukce", blank=True)
    price_of_rec = models.IntegerField(verbose_name="Cena rekonstrukce", null=True, blank=True)
    source_of_finance = models.CharField(max_length=30, blank=True, verbose_name="Zdroj financí")
    owner = models.CharField(max_length=40, blank=True, verbose_name="Vlastník")
    type_of_r = models.CharField(max_length=8, choices=types_choice, blank=True, null=True, verbose_name="Typ památky")
    sign = models.TextField(null=True, blank=True, verbose_name="Nápis")
    body = models.TextField(verbose_name="Popis")
    katalog_numb = models.CharField(max_length=30, blank=True, verbose_name="Rejstříkové č.")
    series_num = models.IntegerField(blank=True, null=True, verbose_name="Pořadová číslo")
    

    # Tags for filtering
    # tohle by melo byt dynamicky...
    w_ssr = models.BooleanField(default=False, verbose_name="Stezka sovy Rozárky")
    w_kc = models.BooleanField(default=False, verbose_name="Křížková cesta")
    w_czp = models.BooleanField(default=False, verbose_name="Cesta za pověstí")
    w_csj = models.BooleanField(default=False, verbose_name="Cesta sv. Jakuba")
    w_div = models.BooleanField(default=False, verbose_name="Cesta divočinou")
    
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
    
    posted = models.DateField(db_index=True, auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Nechat")

    def __str__(self):
        return self.title
