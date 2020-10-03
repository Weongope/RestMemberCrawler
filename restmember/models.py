from django.db import models


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', default="NoName", max_length=10)
    birth_date = models.CharField('Date of Birth', max_length=10)
    birth_place = models.CharField('Place of Birth', max_length=50)
    profession = models.CharField('profession', default="Noprof", max_length=50)
    languages = models.CharField('Known Languages', default="NoLang", max_length=50)
    political_force = models.CharField('Political Force', max_length=50)
    email = models.EmailField('email', blank=False, unique=True, max_length=50)
    
    def __str__(self):
        return self.name

