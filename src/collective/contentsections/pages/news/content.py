from zope.interface import implementer

from collective.contentsections.pages.base import IPage
from collective.contentsections.pages.base import Page


class INewsPage(IPage):
    """NewsPage schema"""


@implementer(INewsPage)
class NewsPage(Page):
    """NewsPage class"""
