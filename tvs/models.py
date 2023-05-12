from django.db import models

from casa7ma_intranet.utils import default_trans


# Create your models here.
class Slide(models.Model):
    name = models.CharField(max_length=255, default='Diapositiva')
    image =  models.ImageField(upload_to='slides/', verbose_name='Imagen')
    image_eng = models.ImageField(upload_to='slides/', verbose_name='Imagen (Inglés)', null=True, blank=True)
    # title = models.CharField(max_length=255, verbose_name='Título')
    # title_en = models.CharField(max_length=255, verbose_name='Título (Inglés)', blank=True, null=True)
    # title_fr = models.CharField(max_length=255, verbose_name='Título (Francés)', blank=True, null=True)
    # title_nl = models.CharField(max_length=255, verbose_name='Título (Neerlandés)', blank=True, null=True)
    # title_de = models.CharField(max_length=255, verbose_name='Título (Alemán)', blank=True, null=True)
    # title_it = models.CharField(max_length=255, verbose_name='Título (Italiano)', blank=True, null=True)
    # title_pt = models.CharField(max_length=255, verbose_name='Título (Portugués)', blank=True, null=True)
    # title_ru = models.CharField(max_length=255, verbose_name='Título (Ruso)', blank=True, null=True)
    # subtitle = models.CharField(max_length=255, verbose_name='Subtítulo')
    # subtitle_en = models.CharField(max_length=255, verbose_name='Subtítulo (Inglés)', blank=True, null=True)
    # subtitle_fr = models.CharField(max_length=255, verbose_name='Subtítulo (Francés)', blank=True, null=True)
    # subtitle_nl = models.CharField(max_length=255, verbose_name='Subtítulo (Neerlandés)', blank=True, null=True)
    # subtitle_de = models.CharField(max_length=255, verbose_name='Subtítulo (Alemán)', blank=True, null=True)
    # subtitle_it = models.CharField(max_length=255, verbose_name='Subtítulo (Italiano)', blank=True, null=True)
    # subtitle_pt = models.CharField(max_length=255, verbose_name='Subtítulo (Portugués)', blank=True, null=True)
    # subtitle_ru = models.CharField(max_length=255, verbose_name='Subtítulo (Ruso)', blank=True, null=True)
    # link = models.CharField(max_length=500, verbose_name='Enlace', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    # def save(self, *args, **kwargs):
    #     try:
    #         if self.title_en == None:
    #             self.title_en = default_trans(self.title, 'en')
    #         if self.title_fr == None:
    #             self.title_fr = default_trans(self.title, 'fr')
    #         if self.title_nl == None:
    #             self.title_nl = default_trans(self.title, 'nl')
    #         if self.title_de == None:
    #             self.title_de = default_trans(self.title, 'de')
    #         if self.title_it == None:
    #             self.title_it = default_trans(self.title, 'it')
    #         if self.title_pt == None:
    #             self.title_pt = default_trans(self.title, 'pt')
    #         if self.title_ru == None:
    #             self.title_ru = default_trans(self.title, 'ru')
    #         if self.subtitle_en == None:
    #             self.subtitle_en = default_trans(self.subtitle, 'en')
    #         if self.subtitle_fr == None:
    #             self.subtitle_fr = default_trans(self.subtitle, 'fr')
    #         if self.subtitle_nl == None:
    #             self.subtitle_nl = default_trans(self.subtitle, 'nl')
    #         if self.subtitle_de == None:
    #             self.subtitle_de = default_trans(self.subtitle, 'de')
    #         if self.subtitle_it == None:
    #             self.subtitle_it = default_trans(self.subtitle, 'it')
    #         if self.subtitle_pt == None:
    #             self.subtitle_pt = default_trans(self.subtitle, 'pt')
    #         if self.subtitle_ru == None:
    #             self.subtitle_ru = default_trans(self.subtitle, 'ru')
    #     finally:
    #         return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Diapositiva'
        verbose_name_plural = 'Diapositivas'


class Room(models.Model):
    LANGUAGE_CHOICES = (
        ('es', 'Español'),
        ('en', 'Inglés'),
        # ('fr', 'Francés'),
        # ('nl', 'Neerlandés'),
        # ('de', 'Alemán'),
        # ('it', 'Italiano'),
        # ('pt', 'Portugués'),
        # ('ru', 'Ruso'),
    )
    name = models.CharField(max_length=255, verbose_name='Nombre')
    name_en = models.CharField(max_length=255, verbose_name='Nombre (Inglés)', blank=True, null=True)
    # name_fr = models.CharField(max_length=255, verbose_name='Nombre (Francés)', blank=True, null=True)
    # name_nl = models.CharField(max_length=255, verbose_name='Nombre (Neerlandés)', blank=True, null=True)
    # name_de = models.CharField(max_length=255, verbose_name='Nombre (Alemán)', blank=True, null=True)
    # name_it = models.CharField(max_length=255, verbose_name='Nombre (Italiano)', blank=True, null=True)
    # name_pt = models.CharField(max_length=255, verbose_name='Nombre (Portugués)', blank=True, null=True)
    # name_ru = models.CharField(max_length=255, verbose_name='Nombre (Ruso)', blank=True, null=True)
    slides = models.ManyToManyField(Slide, verbose_name='Diapositivas')
    language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, verbose_name='Idioma')

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        try:
            if self.name_en == None:
                self.name_en = default_trans(self.name, 'en')
            # if self.name_fr == None:
            #     self.name_fr = default_trans(self.name, 'fr')
            # if self.name_nl == None:
            #     self.name_nl = default_trans(self.name, 'nl')
            # if self.name_de == None:
            #     self.name_de = default_trans(self.name, 'de')
            # if self.name_it == None:
            #     self.name_it = default_trans(self.name, 'it')
            # if self.name_pt == None:
            #     self.name_pt = default_trans(self.name, 'pt')
            # if self.name_ru == None:
            #     self.name_ru = default_trans(self.name, 'ru')
        finally:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'

