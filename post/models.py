from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200)
    ref_url = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    review_time = models.CharField(max_length=200)
    approval_percent = models.CharField(max_length=200)
    addition = models.CharField(max_length=200)
    raiting = models.IntegerField(default=5)
    position = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=50)

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
    company = []

    for comp in list(Post.objects.all()):
        company.append((str(comp.ref_url), str(comp.title)))
    pos = [('alert_left', 'Left'), ('alert_right', 'Right')]

    text = models.TextField(max_length=200)
    position = models.CharField(choices=pos, default='-', max_length=30)
    company_name = models.CharField(choices=company, default='-', max_length=255)

    def __str__(self):
        return '%s %s %s' % (
            self.position, self.text, self.get_company_name_display()
        )


class Review(models.Model):
    company = []
    for comp in list(Post.objects.all()):
        company.append((str(comp.ref_url), str(comp.title)))

    rating = [(x, str(x)) for x in range(1, 6)]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=4000)
    company_name = models.CharField(choices=company, default='-', max_length=255)
    company_rating = models.IntegerField(choices=rating, default=5)
    time = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.approved, self.email, self.name, self.get_company_name_display())


class Statistic(models.Model):
    title = models.CharField(max_length=200, default='None')

    def __str__(self):
        return '%s' % (self.title)
