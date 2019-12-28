from django.db import models


class Redirect(models.Model):
    title = models.CharField(max_length=200)
    ref_url = models.CharField(max_length=300)

    def __str__(self):
        return '%s' % (
            self.title
        )
