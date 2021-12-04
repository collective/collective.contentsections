from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class ILinksSection(ISection):
    """LinksSection schema"""


@implementer(ILinksSection)
class LinksSection(Section):
    """LinksSection content type"""
