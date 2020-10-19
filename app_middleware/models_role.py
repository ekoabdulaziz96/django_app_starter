from django.db import models
from django.utils.text import slugify
# from django.http import JsonResponse


class Role(models.Model):
    # YA = '1'
    # TIDAK = '0'

    # ROLE_CHOICES = (
    #     (YA, 'Ya'),
    #     (TIDAK, 'Tidak'),
    # )
    nama = models.CharField(max_length=200)
    # deskripsi = models.TextField(default='-')
    # pcreate = models.CharField(max_length=255, choices=ROLE_CHOICES,default=YA)
    # pread = models.CharField(max_length=255,choices=ROLE_CHOICES,default=YA)
    # pupdate = models.CharField(max_length=255, choices=ROLE_CHOICES,default=YA)
    # pdelete = models.CharField(max_length=255, choices=ROLE_CHOICES,default=YA)

    slug = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.nama)
        super(Role, self).save()

    def __str__(self):
        return "[{}] Role {}".format(self.id,self.nama)