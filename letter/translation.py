from modeltranslation.translator import register, TranslationOptions
from letter.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'text',)


