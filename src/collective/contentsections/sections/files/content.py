from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IFilesSection(IBaseLinksSection):
    """FilesSection schema"""


@implementer(IFilesSection)
class FilesSection(Section):
    """FilesSection content type"""
