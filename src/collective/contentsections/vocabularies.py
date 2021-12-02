from operator import itemgetter

from collective.contentsections import _
from plone import api
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

IMAGE_ALIGNMENTS = {
    "left": _("Left"),
    "right": _("Right"),
    "bottom": _("Bottom"),
    "top": _("Top"),
}
IMAGE_SIZES = {
    "large": _("Large"),
    "preview": _("Preview"),
    "mini": _("Mini"),
}
SECTION_WIDTHS = {
    12: _("Container 1/1"),
    9: _("Container 3/4"),
    8: _("Container 2/3"),
    6: _("Container 1/2"),
    4: _("Container 1/3"),
    3: _("Container 1/4"),
    0: _("Full page width"),
}


class VocabularyFactory:
    def __init__(self, terms):
        self.terms = terms

    def __call__(self, context=None):
        terms = [SimpleTerm(value=key, token=key, title=title) for key, title in self.terms.items()]
        return SimpleVocabulary(terms)


ImageAlignmentsVocabulary = VocabularyFactory(IMAGE_ALIGNMENTS)
ImageSizesVocabulary = VocabularyFactory(IMAGE_SIZES)
SectionWidthsVocabulary = VocabularyFactory(SECTION_WIDTHS)


class IconsVocabularyFactory:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, context=None):
        registry = getUtility(IRegistry)
        items = [
            (key.replace(self.prefix, ""), record.field.title)
            for key, record in registry.records.items()
            if key.startswith(self.prefix)
        ]
        items.sort(key=itemgetter(1))
        terms = [SimpleTerm(value=key, token=key, title=title) for key, title in items]
        return SimpleVocabulary(terms)


LeadIconsVocabulary = IconsVocabularyFactory("plone.icon.")
