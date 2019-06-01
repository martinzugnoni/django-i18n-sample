from modeltranslation.translator import translator, TranslationOptions
from core.models import HomePage, AboutPage


class HomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class AboutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(HomePage, HomePageTranslationOptions)
translator.register(AboutPage, AboutPageTranslationOptions)
