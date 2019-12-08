from django.db import models
from post.models import Compony
from datetime import datetime


class Review(models.Model):
    rating = [(x, str(x)) for x in range(1, 6)]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=4000)
    company_name = models.ForeignKey(
        Compony,
        on_delete=models.CASCADE,
        default="",
        blank=True,
        null=True,
    )
    company_rating = models.IntegerField(choices=rating, default=5)
    time = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s, %s' % (
            self.approved,
            self.email,
            self.name,
            self.company_name
        )
