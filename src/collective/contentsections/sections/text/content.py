from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from plone.autoform import directives
from zope.interface import implementer


class ITextSection(ISection):
    """TextSection schema"""

    image_alignment = schema.Choice(
        title=_(u"Image alignment"),
        vocabulary="collective.contentsections.ImageAlignments",
        default="left",
        required=True,
    )
    image_size = schema.Choice(
        title=_(u"Image size"),
        vocabulary="collective.contentsections.ImageSizes",
        default="preview",
        required=True,
    )

    directives.order_before(image_alignment="IVersionable.changeNote")
    directives.order_after(image_size="image_alignment")


@implementer(ITextSection)
class TextSection(Section):
    """TextSection content type"""
