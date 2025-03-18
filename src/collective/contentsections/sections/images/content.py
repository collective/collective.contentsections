from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section


class IImagesSection(IBaseLinksSection):
    """ImagesSection schema"""


@implementer(IImagesSection)
class ImagesSection(Section):
    """ImagesSection content type"""
