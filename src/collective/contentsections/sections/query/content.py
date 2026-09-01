from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IQuerySection(IBaseLinksSection):
    """QuerySection schema"""


@implementer(IQuerySection)
class QuerySection(Section):
    """QuerySection content type"""
