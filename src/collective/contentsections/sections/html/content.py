from plone import schema
from zope.interface import implementer

from ..base import ISection
from ..base import Section


class ISectionHTML(ISection):
    """Marker interface and Dexterity Python Schema for SectionHTML"""

    html = schema.SourceText(
        title=u"HTML",
        required=True,
    )


@implementer(ISectionHTML)
class SectionHTML(Section):
    """SectionHTML class"""
