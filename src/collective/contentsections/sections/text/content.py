from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from plone.autoform import directives
from zope.interface import implementer


class ITextSection(ISection):
    """TextSection schema"""

    lead_image_alignment = schema.Choice(
        title=_(u"Image alignment"),
        vocabulary="collective.contentsections.ImageAlignments",
        default="left",
        required=True,
    )
    lead_image_scale = schema.Choice(
        title=_(u"Image scale"),
        vocabulary="plone.app.vocabularies.ImagesScales",
        default="preview",
        required=True,
    )

    directives.order_before(lead_image_alignment="IVersionable.changeNote")
    directives.order_after(lead_image_scale="image_alignment")


@implementer(ITextSection)
class TextSection(Section):
    """TextSection content type"""
