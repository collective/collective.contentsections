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
COLUMN_WIDTHS = {
    0: "",
    3: _("1/4"),
    4: _("1/3"),
    6: _("1/2"),
    8: _("2/3"),
    9: _("3/4"),
    12: _("1/1"),
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
ColumnWidthsVocabulary = VocabularyFactory(COLUMN_WIDTHS)
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
