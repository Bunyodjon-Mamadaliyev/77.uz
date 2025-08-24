from modeltranslation.translator import TranslationOptions, register

from .models import Common, District, Region


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Common)
class CommonTranslationOptions(TranslationOptions):
    fields = ("title",)
