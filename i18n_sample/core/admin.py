from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import HomePage, AboutPage


class HomePageAdmin(TranslationAdmin):
    pass


class AboutPageAdmin(TranslationAdmin):
    pass


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
