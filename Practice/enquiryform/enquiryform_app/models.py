from django.db import models
from multiselectfield import MultiSelectField


class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    SKILL_CHOICES = (('py', 'PYTHON'),
                     ('dj', 'DJANGO'),
                     ('ra', 'RESTAPI'),
                     ('ui', 'UI')

                      )
    skills = MultiSelectField(max_length=100, choices=SKILL_CHOICES)

    LOCATION_CHOICES = (('hyd', 'Hyderabad'),
                        ('bang', 'Bangalore'),
                        ('che', 'Chennai'),
                        ('pun', 'Pune')

                        )
    location = MultiSelectField(max_length=100, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
