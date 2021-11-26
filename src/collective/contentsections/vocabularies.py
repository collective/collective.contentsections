from collective.contentsections import _
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
    "col-sm-3": _("Quarter of width"),
    "col-sm-4": _("Third of width"),
    "col-sm-6": _("Half of width"),
    "col-sm-8": _("Two third of width"),
    "col-sm-9": _("Three quarter of width"),
    "col-sm-12": _("Full width"),
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
