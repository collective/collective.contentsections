from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IImagesSection(IBaseLinksSection):
    """ImagesSection schema"""


@implementer(IImagesSection)
class ImagesSection(Section):
    """ImagesSection content type"""
