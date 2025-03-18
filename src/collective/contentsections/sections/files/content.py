from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section


class IFilesSection(IBaseLinksSection):
    """FilesSection schema"""


@implementer(IFilesSection)
class FilesSection(Section):
    """FilesSection content type"""
