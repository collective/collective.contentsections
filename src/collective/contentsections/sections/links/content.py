from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class ILinksSection(IBaseLinksSection):
    """LinksSection schema"""


@implementer(ILinksSection)
class LinksSection(Section):
    """LinksSection content type"""
