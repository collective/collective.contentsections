from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from plone.autoform import directives
from zope.interface import implementer


class ITextSection(ISection):
    """TextSection schema"""

    lead_image_alignment = schema.Choice(
        title=_("Lead image alignment"),
        vocabulary="collective.contentsections.ImageAlignments",
        default="right",
    )
    lead_image_width = schema.Choice(
        title=_("Lead image width"),
        vocabulary="collective.contentsections.LeadImageWidths",
        default=4,
    )

    directives.order_before(lead_image_alignment="IVersionable.changeNote")
    directives.order_after(lead_image_width="lead_image_alignment")


@implementer(ITextSection)
class TextSection(Section):
    """TextSection content type"""
