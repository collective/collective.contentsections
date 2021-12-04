from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IFilesSection(ISection):
    """FilesSection schema"""


@implementer(IFilesSection)
class FilesSection(Section):
    """FilesSection content type"""
