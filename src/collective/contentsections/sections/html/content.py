from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from zope.interface import implementer


class IHTMLSection(ISection):
    """HTMLSection schema"""

    html = schema.SourceText(
        title=_(u"HTML"),
    )


@implementer(IHTMLSection)
class HTMLSection(Section):
    """HTMLSection content type"""
