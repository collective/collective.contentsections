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
CONTAINER_WIDTHS = {
    12: _("Container 100%"),
    8: _("Container 66%"),
    6: _("Container 50%"),
    0: _("Window 100%"),
}
COLUMN_ALIGNMENTS = {
    "start": _("Start"),
    "center": _("Center"),
    "end": _("End"),
}


class VocabularyFactory:
    def __init__(self, terms):
        self.terms = terms

    def __call__(self, context=None):
        terms = [SimpleTerm(value=value, token=str(value), title=title) for value, title in self.terms.items()]
        return SimpleVocabulary(terms)


ImageAlignmentsVocabulary = VocabularyFactory(IMAGE_ALIGNMENTS)
ContainerWidthsVocabulary = VocabularyFactory(CONTAINER_WIDTHS)
ColumnAlignmentsVocabulary = VocabularyFactory(COLUMN_ALIGNMENTS)


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
        terms = [SimpleTerm(value=value, token=str(value), title=title) for value, title in items]
        return SimpleVocabulary(terms)


LeadIconsVocabulary = IconsVocabularyFactory("plone.icon.")
