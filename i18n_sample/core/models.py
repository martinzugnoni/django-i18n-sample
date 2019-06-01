from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        abstract = True


class HomePage(Page):
    pass


class AboutPage(Page):
    pass
