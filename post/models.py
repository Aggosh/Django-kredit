from django.db import models
from datetime import datetime


class Compony(models.Model):
    rating = [(x, str(x)) for x in range(1, 6)]

    title = models.CharField(max_length=200)
    ref_url = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    review_time = models.CharField(max_length=200)
    approval_percent = models.CharField(max_length=200)
    addition = models.CharField(max_length=200)
    raiting = models.IntegerField(choices=rating, default=5)
    position = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=50)
    main_photo = models.ImageField(
        upload_to='compony/img',
        height_field=None,
        width_field=None,
        max_length=100,
        default="",
        verbose_name='Фото',
    )

    def __str__(self):
        return 'Position %s Name: %s URL: %s' % (
            self.position, self.title, self.ref_url
        )


class Advertising(models.Model):
    title = models.CharField(max_length=200)
    ref_url = models.CharField(max_length=200)
    img_name = models.CharField(max_length=200)
    position = models.IntegerField(default=1)

    def __str__(self):
        return 'Position %s "%s", URL: %s' % (
            self.position, self.title, self.ref_url
        )


class Notification(models.Model):
    pos = [('alert_left', 'Left'), ('alert_right', 'Right')]

    text = models.TextField(max_length=200)
    position = models.CharField(choices=pos, default='', max_length=30)
    company_nama = models.ForeignKey(
        Compony,
        on_delete=models.CASCADE,
        default="",
        blank=True,
        null=True
    )

    def __str__(self):
        return '%s %s %s' % (
            self.position, self.text, self.company_nama
        )


class Review(models.Model):
    rating = [(x, str(x)) for x in range(1, 6)]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=4000)
    company_nama = models.ForeignKey(
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
            self.company_nama
        )
