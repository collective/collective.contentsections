from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from plone.autoform import directives
from zope.interface import implementer


class ITextSection(ISection):
    """TextSection schema"""

    lead_image_alignment = schema.Choice(
        title=_(u"Lead image alignment"),
        vocabulary="collective.contentsections.ImageAlignments",
        default="right",
    )
    lead_image_scale = schema.Choice(
        title=_(u"Lead image scale"),
        vocabulary="plone.app.vocabularies.ImagesScales",
        default="preview",
    )

    directives.order_before(lead_image_alignment="IVersionable.changeNote")
    directives.order_after(lead_image_scale="lead_image_alignment")


@implementer(ITextSection)
class TextSection(Section):
    """TextSection content type"""
