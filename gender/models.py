from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gender'
        managed = True
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
