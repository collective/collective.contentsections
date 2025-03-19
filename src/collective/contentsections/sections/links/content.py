from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section


class ILinksSection(IBaseLinksSection):
    """LinksSection schema"""


@implementer(ILinksSection)
class LinksSection(Section):
    """LinksSection content type"""
