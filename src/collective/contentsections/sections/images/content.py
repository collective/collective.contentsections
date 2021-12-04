from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IImagesSection(ISection):
    """ImagesSection schema"""


@implementer(IImagesSection)
class ImagesSection(Section):
    """ImagesSection content type"""
