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
SECTION_WIDTHS = {
    "quarter": _("Quarter of page"),
    "third": _("Third of page"),
    "half": _("Half of page"),
    "two-thirds": _("Two thirds of page"),
    "three-quarters": _("Three quarters of page"),
    "full": _("Full page"),
    "screen": _("Full screen"),
}


class VocabularyFactory:
    def __init__(self, terms):
        self.terms = terms

    def __call__(self, context=None):
        terms = [SimpleTerm(value=key, token=key, title=title) for key, title in self.terms.items()]
        return SimpleVocabulary(terms)


ImageAlignmentsVocabulary = VocabularyFactory(IMAGE_ALIGNMENTS)
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
